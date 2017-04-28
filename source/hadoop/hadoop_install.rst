Hadoop 2.8.0 半自动化安装
==================================


1, 虚拟机准备 
---------------


| 俺使用 VirtualBox 创建了 3 台虚拟机，分别叫 `ubuntu-1`, `ubuntu-2`, `ubuntu-3` 。  
| 均配置了 4 个网卡, 网卡模式有 桥接模式，内部模式 还有 内部模式。
| 桥接模式可以供宿主机访问，内部模式用于 3 台虚机之间访问。
| 内部模式的主机分别为 `ubuntu-1 10.10.10.1`,  `ubuntu-2 10.10.10.2`,  `ubuntu-3 10.10.10.3` 。


2, Hadoop 分发
----------------------------

| 安装分布式软件最让新手头疼的是，一台机器一台机器地登录上去，一条命令一条命令的执行，非常耗时间，让学习的热情一下子冷却了一半。
| 所幸，我们可以借助运维神器 `ansible` 一键 完成机器的初始化工作。
| ansible 有一个 playbook 的概念，有点像写剧本的意味。我编写了一个如下的play:

**play.yml**::

	---
	- hosts: taoge-ubuntu
	  tasks:
	  - name: create hadoop user and generate ssh key
	    user:
	        name: hadoop
	        password: hadoop
	        shell: /bin/bash
	        generate_ssh_key: yes
	        ssh_key_bits: 2048
	        ssh_key_file: .ssh/id_rsa

	  - name: add authorize key to slaves
	    authorized_key:
	        user: hadoop
	        state: present
	        key: "{{ lookup('file', '/home/hadoop/.ssh/id_rsa.pub')}}"


	  - name: copy hadoop-2.8.0.tar.gz
	    copy:
	        src: /root/hadoop-2.8.0.tar.gz
	        dest: /home/hadoop/hadoop-2.8.0.tar.gz
	        owner: hadoop
	        mode: 0644

	  - name: unarchive hadoop-2.8.0.tar.gz
	    unarchive:
	        src: /home/hadoop/hadoop-2.8.0.tar.gz
	        dest: /home/hadoop/
	        remote_src: True

	  - name: add /etc/hosts
	    lineinfile:
	        path: /etc/hosts
	        line: '10.10.10.1	hadoop-1'

	  - name: add /etc/hosts
	    lineinfile:
	        path: /etc/hosts
	        line: '10.10.10.2	hadoop-2'

	  - name: add /etc/hosts
	    lineinfile:
	        path: /etc/hosts
	        line: '10.10.10.3	hadoop-3'

	  - name: add JAVA_HOME
	    lineinfile:
	        path: /home/hadoop/.bashrc
	        line: 'export JAVA_HOME=/opt/jdk1.8.0_131/'


3, Hadoop 配置
-------------------------

| Hadoop 配置使用了 XML 格式，为什么用 XML 而不用其它的格式呢？这是个好问题。
| 配置 DFS 的话，只要配置 两个文件: `core-site.xml`, `hdfs-site.xml`。 配置文件都在 etc/hadoop 文件夹里。
| `core-site.xml` 在 三节点设置都一样， `hdfs-site.xml` 在 namenode 和 datanode 不一样。
| 我的一些配置如下:

**NameNode**::

	core-site.xml: 

	<configuration>
	    <property>
	        <name>fs.defaultFS</name>
	        <value>hdfs://hadoop-1:9000</value>
	    </property>

	</configuration>

    
	hdfs-site.xml

	<configuration>
	    <property>
	            <name>dfs.replication</name>
	            <value>2</value>
	    </property>

	    <property>
	            <name>dfs.namenode.name.dir</name>
	            <value>/home/hadoop/nn</value>
	    </property>

	    <property>
	            <name>dfs.namenode.handler.count</name>
	            <value>10</value>
	    </property>

	    <property>
	            <name>dfs.hosts</name>
	    	    <value>/home/hadoop/hadoop-2.8.0/hosts</value>
	    </property>

	</configuration>


**DataNode**::

	hdfs-xite.xml

	<configuration>
	    <property>
	            <name>dfs.replication</name>
	            <value>2</value>
	    </property>

	    <property>
	            <name>dfs.datanode.data.dir</name>
	            <value>/home/hadoop/dd</value>
	    </property>

	</configuration>



4, Up, Up, Up !
---------------------

| Hadoop 的分布式存储系统是 `Master-Slave` 模式，也就是一个包工头和多个工人协作的模式。 
| 所以节点类型有 2 种: `NameNode`, `DataNode`, 也就是控制流和数据流的区别。
| 俺设置的是 `NameNode` 是 `hadoop-1`, `DataNode` 是 `hadoop-2` 和 `hadoop-3` 。
| 在 `NameNode` 上执行:  `bin/hdfs  namenode > namenode.log 2>&1 &`
| 在 `DataNode` 上执行:  `bin/hdfs  datanode > datanode.log 2>&1 &`
| 好，现在 Hadoop DFS 已经搭建起来了！
| 欢迎来到大数据的世界。 让大象撑爆您的容器或虚拟机吧！










Q&A: 为什么我遇到了网上没有的问题?
--------------------------------------
| 不可避免的，凡是学习一个新东西，总会有老手都知道，而新手百思不得其解的问题。
| 这时候就是考验 DEBUG 的能力的时候。
| 对此俺只有一个忠告 : 多喝水，仔细看日志。


- DataNode 不能连接到 NameNode, 连接被拒绝 ？

	一般情况下，NameNode 监听端口时绑定的 host 可能不同。比如 绑定localhost的时候只有本地可以访问。

- NameNode 启动总是显示 dfs 的文件夹为空 file:///  ？

	很有可能启动时没有读取正确的配置，可以使用 ` bin/hdfs getconf` 这个命令来查看配置是否是自己写的配置。 




.. feed-entry::
	   :author: Taoge
	   :date: 2017-04-28

	
	






