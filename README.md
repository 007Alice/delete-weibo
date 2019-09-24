
# delete-weibo
delete_weibo.py



root@kali:/home/Alice007# python delete_weibo.py -h
Usage: delete_weibo.py [options]

Options:
  -h, --help         show this help message and exit
  -u USR, --usr=USR  your username of weibo
  -p PWD, --pwd=PWD  your password of weibo
  -n NUM, --num=NUM  the number to delete at once. default num is 10.



交互式删除微博，默认一次删除的条数为10。 

删除 n 条之后，会提示是否继续删除 continue delete or quit?(c/q) ：

    c 为继续删 n 条；
    q 为退出。
  
  
root@kali:/home/Alice007# python delete_weibo.py -u username -p password


可设置一次性删除的条数，如20条。如果该数字超过页面显示的微博数量，则需要在脚本中新增一个循环，加上 weibo.refresh() 。

root@kali:/home/Alice007# python delete_weibo.py -u username -p password -n 20
