"""Quick hack to (a) demo the synchronous APIs and (b) dump all records."""

import time

from demo.main import model, context, tasklets, Message, Account, account_key


class LogRecord(model.Model):
  timestamp = model.FloatProperty()


@context.toplevel
def main():
  print 'Content-type: text/plain'
  print
  qry = Message.query().order(-Message.when)
  for msg in qry:
    print msg.userid, time.ctime(msg.when), repr(msg.body)
    if msg.userid is not None:
      act = account_key(msg.userid).get()
      if act is None:
        print '  * Bad account'
      else:
        print '  * Account', act.nickname, act.email
  log = LogRecord(timestamp=time.time())
  log.put_async()


if __name__ == '__main__':
  main()
