from datetime import datetime

from sqlalchemy import Column, BigInteger, Integer, ForeignKey, DateTime, SmallInteger, String
from sqlalchemy.orm import relationship

from api.models.base import Base


class SignInOrder(Base):
    id=Column(BigInteger,autoincrement=True,primary_key=True)

    pubPersonId=Column(BigInteger,ForeignKey('user.userid'))
    pubPerson=relationship('User',back_populates='pubSignIns')

    pubTime=Column(DateTime)
    endTime=Column(DateTime)
    # DateTime datetime.datetime 日期和时间

    needtoSignIn=Column(Integer)
    haveSignIn=Column(Integer)

    signInStatus=Column(SmallInteger,default=1)
    qrcodeUrl=Column(String(100))#本地的相对路径

    signInPerson=relationship(BigInteger,ForeignKey('signInOrder'))#一对多的一侧

    def generate_pubTime(self):
        self.pubTime=datetime.now()#todo 可能有误类型错误