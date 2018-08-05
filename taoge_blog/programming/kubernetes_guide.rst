[Draft] Kubernetes 搭车客指南
===============================

.. meta::

   :description: taoge 写的 kubernetes 搭车客指南
   :keywords: kubernetes, kubernetes 源码, kubernetes 指南, kubernetes 设计原则

本文对符合以下特征任一的人不适合阅读:

- 精通 kubenetes 的 SRE (Senior Reboot Engineer)
- 十年以上工作经验的云计算从业人员
- 写得一手好代码 (复制粘贴, 能跑就行)




Kubernetes 的设计原则
----------------------------

它很简单, 就是不断比较期望值与实际值, 最终达到收敛的过程. Maybe 有点像梯度下降算法的爬山过程.




Kubernetes 的几个组件
------------------------

- apiserver
- schduler
- controller
- kubelet







FAQ
--------------------

1, Kubernetes 高可用是怎么做的
2, 谈谈 Kubernetes 的缓存
3, 什么是 List-Watch 
4, Kubernetes 是否过于复杂了






.. feed-entry::
	   :author: Taoge
	   :date: 2018/07/26

