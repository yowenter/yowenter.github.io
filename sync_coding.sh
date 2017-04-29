set -x 

rm -rf /tmp/yowenter.github.io
cp -r /Users/wenter/private-repos/yowenter.github.io /tmp/yowenter.github.io

rm -rf /tmp/yowenter.github.io/.git

cp -rf /tmp/yowenter.github.io/* /Users/wenter/private-repos/blog/

cd /Users/wenter/private-repos/blog/

git add .
git commit -m "+ sync from github "
git push







