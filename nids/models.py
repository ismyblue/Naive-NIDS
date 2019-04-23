from django.db import models


class UnsignedIntegerField(models.IntegerField):
    """
    自定义无符号整数字段
    """
    def db_type(self, connection):
        return 'int unsigned'


class UnsignedTinyIntegerField(models.IntegerField):
    """
    自定义无符号tinyint
    """
    def db_type(self, connection):
        return 'tinyint unsigned'


class TinyIntegerField(models.IntegerField):
    """
    自定义tinyint
    """
    def db_type(self, connection):
        return 'tinyint'


class UnsignedSmallIntegerField(models.IntegerField):
    """
    自定义无符号smallint
    """
    def db_type(self, connection):
        return 'smallint unsigned'


# #  Create your models here.
class Schema(models.Model):
    """
    Snort schema表 Self-documented information about the database
    关于数据库的自文档化信息
    """
    vseq = UnsignedIntegerField(primary_key=True) # 数据库模式ID号(例如。' 102 ')
    ctime = models.DateTimeField(blank=False) # Timestamp of database creation time 数据库创建时间的时间戳

    class Meta:
        db_table = 'schema'


class Event(models.Model):
    """
    Meta-data（元数据） about the detected alert
    """
    sid = UnsignedIntegerField() # Sensor ID
    cid = UnsignedIntegerField(primary_key=True) # Event ID
    signature = UnsignedIntegerField(db_index=True) # Signature:对应signature表格中的sig_id选项，表明这条告警事件所属的规则形式的告警对应哪一类rules。
    timestamp = models.DateTimeField(db_index=True) # Timestamp:对应告警事件发生的系统时间。
    class Meta:
        db_table = 'event'
        unique_together = (("sid", "cid"),)
        indexes = [
            models.Index(
                fields=['signature'],
                name='sig',
            ),
            models.Index(
                fields=['timestamp'],
                name='time',
            ),
        ]


class Signature(models.Model):
    """
  	Normalized listing of alert/signature names, priorities, and revision IDs
  	警报/签名名称、优先级和修订id的规范化列表
    有规则形式的告警信息，按种类分类。
    """
    sig_id = UnsignedIntegerField(primary_key=True) # 自增Signature ID 总数代表发生告警种类的总数。是告警种类的主码。
    sig_name = models.CharField(max_length=255) # Signature Name 告警名称。对应每条alert语句的Msg。
    sig_class_id = UnsignedIntegerField() # Classification ID 对应sig_class表格中的sig_class_id.代表告警种类的大类信息。
    sig_priority = UnsignedIntegerField(blank=True) # Priority 告警的优先级
    sig_rev = UnsignedIntegerField(blank=True) # Revision number 版本号
    sig_sid = UnsignedIntegerField(blank=True) # Internal signature ID 内部signatureID
    sig_gid = UnsignedIntegerField(blank=True) # 全局signatureID
    class Meta:
        db_table = 'signature'
        indexes = [
            models.Index(
                fields=['sig_name'],
                name='sign_idx',
            ),
            models.Index(
                fields=['sig_class_id'],
                name='sig_class_id_idx',
            ),
        ]


class Sig_reference(models.Model):
    """
    Reference information for a signature
    签名的参考信息
    sig_reference：提供报警种类信息signature的参考信息。将signature与reference联系起来的表格
    """
    sig_id = UnsignedIntegerField(primary_key=True) # Signature ID Sig_id:对应的告警种类。
    ref_seq = UnsignedIntegerField() # Reference sequence number (multiple references)    Ref_id:对应reference表格中的主码
    ref_id = UnsignedIntegerField() # Reference ID 参考序列号
    class Meta:
        db_table = 'sig_reference'
        unique_together = (("sig_id", "ref_seq"),)


class Reference(models.Model):
    """
    Reference IDs for a signature
    Reference:提供一些支持信息
    """
    ref_id = UnsignedIntegerField(primary_key=True) # Reference ID
    ref_system_id = UnsignedIntegerField() # Reference system ID Ref_system_id:对应reference_system表格
    ref_tag = UnsignedIntegerField() # Reference tag (e.g. CVE-CAN-2001-01) Ref_tag:关于reference的一些信息
    class Meta:
        db_table = 'reference'


class Reference_system(models.Model):
    """
    (lookup table) Reference system list
    (查询表)参考系统列表
    """
    ref_system_id = UnsignedIntegerField(primary_key=True) # Reference system ID
    ref_system_name = models.CharField(max_length=20, blank=True) # Reference system name (e.g. CVE)
    class Meta:
        db_table = 'reference_system'


class Sig_class(models.Model):
    """
    Normalized listing of alert/signature classifications
    警报/签名分类的规范化列表
    """
    sig_class_id = UnsignedIntegerField(primary_key=True, db_index=True) # Signature classification ID
    sig_class_name = models.CharField(max_length=60, db_index= True) # Classification name (e.g. recon)
    class Meta:
        db_table = 'sig_class'


class Sensor(models.Model):
    """
    Sensor name传感器名字
    store info about the sensor supplying data 存储传感器提供数据的信息
    """
    sid = UnsignedIntegerField(primary_key=True) #  Sensor ID
    hostname = models.TextField(blank=True) # Hostname of the sensor (IP if can't qualify)
    interface = models.TextField(blank=True) # Network interface (e.g. eth0)
    filter = models.TextField(blank=True)  # BPF filter
    detail = TinyIntegerField(blank=True) # Detail level of the logging
    encoding = TinyIntegerField(blank=True) # Encoding format of the payload
    last_cid = UnsignedTinyIntegerField() # 对应每个sid即传感器捕获告警的最后一个值
    class Meta:
        db_table = 'sensor'


class Iphdr(models.Model):
    """
    IP protocol fields
    All of the fields of an ip header
    ip数据包首部信息
    """
    sid = UnsignedIntegerField()
    cid = UnsignedIntegerField(primary_key=True)
    ip_src = UnsignedIntegerField() # ip数据包源地址
    ip_dst = UnsignedIntegerField() # ip数据包目的地址
    ip_ver = UnsignedTinyIntegerField(blank=True) # ip数据包版本，一般为ipv4即为4
    ip_hlen = UnsignedTinyIntegerField(blank=True) # _hlen: ip数据包首部长度，以DWORD为单位，通常为5，共20个字节。（IP数据包最长可为4*15=60字节）。
    ip_tos = UnsignedTinyIntegerField(blank=True) # ip_tos: ip数据包服务类型。共8位，其每位的含义见“项目相关/各类数据包格式”。
    ip_len = UnsignedSmallIntegerField(blank=True) # ip_len: ip数据包的总长度，包括ip数据包头
    ip_id = UnsignedSmallIntegerField(blank=True) # ip_id: ip数据包的标识符
    ip_flags = UnsignedTinyIntegerField(blank=True) # ip_flags: ip数据包的标志
    ip_off = UnsignedSmallIntegerField(blank=True)#  ip_off: 如果ip数据包分段，则此段用于指明分段在原ip数据包中位置
    ip_ttl = UnsignedTinyIntegerField(blank=True) # ip_ttl: ip数据包的生存周期
    ip_proto = UnsignedTinyIntegerField() # ip_proto: ip数据包的上层协议ICMP(1)、TCP(6)、UDP(17)
    ip_csum = UnsignedSmallIntegerField(blank=True) #  ip_csum: ip数据包首部检查和
    class Meta:
        db_table = 'iphdr'
        unique_together = (("sid", "cid"),)
        indexes = [
            models.Index(
                fields=['ip_src'],
                name='ip_src'
            ),
            models.Index(
                fields=['ip_dst'],
                name='ip_dst'
            )
        ]


class Tcphdr(models.Model):
    """
     All of the fields of a tcp header
     tcphdr: tcp协议数据包报文首部信息
    """
    sid = UnsignedIntegerField()
    cid = UnsignedIntegerField(primary_key=True)
    tcp_sport = UnsignedSmallIntegerField() #  tcp_sport,tcp-dport：源与目的端口号
    tcp_dport = UnsignedSmallIntegerField()
    tcp_seq = UnsignedIntegerField(blank=True) # tcp_seq,tcp_ack: tcp序列号与确认号
    tcp_ack = UnsignedIntegerField(blank=True)
    tcp_off = UnsignedTinyIntegerField(blank=True) #  tcp_off：报文首部长度（4bit），以DWORD为单位
    tcp_res = UnsignedTinyIntegerField(blank=True) #  tcp_res: tcp首部保留字段
    tcp_flags = UnsignedTinyIntegerField() #   tcp_flags: 6bit的标志字段（URG,ACK,PSH,RST,SYN,FIN）
    tcp_win = UnsignedSmallIntegerField(blank=True) #  tcp_win: tcp接受窗口大小
    tcp_csum = UnsignedSmallIntegerField(blank=True) #   tcp_csum: tcp校验和字段
    tcp_urp = UnsignedSmallIntegerField(blank=True) # tcp_urp: tcp紧急数据指针
    class Meta:
        db_table = 'tcphdr'
        unique_together = (("sid", "cid"),)
        indexes = [
            models.Index(
                fields=['tcp_sport'],
                name='tcp_sport'
            ),
            models.Index(
                fields=['tcp_dport'],
                name='tcp_dport'
            ),
            models.Index(
                fields=['tcp_flags'],
                name='tcp_flags'
            ),
        ]


class Udphdr(models.Model):
    """
    All of the fields of a udp header
    udphdr: udp协议数据包首部信息
    """
    sid = UnsignedIntegerField()
    cid = UnsignedIntegerField(primary_key=True)
    udp_sport = UnsignedSmallIntegerField() # udp_sport,udp_dport:udp源端口与目的端口号
    udp_dport = UnsignedSmallIntegerField()
    udp_len = UnsignedSmallIntegerField(blank=True) # udp_len:包括udp首部在内的udp报文的长度，以字节为单位
    udp_csum = UnsignedSmallIntegerField(blank=True) # upd_csum:udp首部检查和字段
    class Meta:
        db_table = 'udphdr'
        unique_together = (("sid", "cid"),)
        indexes = [
            models.Index(
                fields=['udp_sport'],
                name='udp_sport'
            ),
            models.Index(
                fields=['udp_dport'],
                name='udp_dport'
            ),
        ]


class Icmphdr(models.Model):
    """
    All of the fields of an icmp header
    icmphdr:
    """
    sid = UnsignedIntegerField()
    cid = UnsignedIntegerField(primary_key=True)
    icmp_type = UnsignedTinyIntegerField() # icmp_type:icmp报文类型字段，占一个字节
    icmp_code  = UnsignedTinyIntegerField() # icmp_code:icmp报文编码字段，占一个字节
    icmp_csum = UnsignedSmallIntegerField(blank=True) # icmp_csum:icmp校验和字段，占两个字节。校验包括数据载荷在内的整个ICMP报文的正确性。
    icmp_id = UnsignedSmallIntegerField(blank=True) # icmp_id:icmp报文标示符
    icmp_seq = UnsignedSmallIntegerField(blank=True) # icmp_seq:icmp序列号字段
    class Meta:
        db_table = 'icmphdr'
        unique_together = (("sid", "cid"),)
        indexes = [
            models.Index(
                fields=['icmp_type'],
                name='icmp_type'
            )
        ]


class Opt(models.Model):
    """
    Protocol options
    opt: 关于ip 和tcp的一些选择信息
    """
    sid = UnsignedIntegerField()
    cid = UnsignedIntegerField(primary_key=True)
    optid = UnsignedIntegerField()
    opt_proto = UnsignedTinyIntegerField() # 对应ip数据包中的tos字段。一般为6，代表是tcp协议。
    opt_code = UnsignedTinyIntegerField()
    opt_len = UnsignedSmallIntegerField(blank=True)
    opt_data = models.TextField(blank=True)
    class Meta:
        db_table = 'opt'
        unique_together = (("sid", "cid", "optid"),)


class Data(models.Model):
    """
    Snort Data表，抓取的数据包内容
    Packet payload
    """
    sid = UnsignedIntegerField() # 不允许为空 null=True是说当字段为Empty时，用NUll代替
    cid = UnsignedIntegerField(primary_key=True) # 不允许为空
    data_payload = models.TextField(blank=True) # data_payload:数据包有效载荷
    class Meta:
        db_table = 'data'
        unique_together = (("sid", "cid"),)


class Encoding(models.Model):
    """
    encoding is a lookup table for storing encoding types
    编码是用于存储编码类型的查找表
    encoding:数据包中数据的存在形式
    0- Hex
    1- base64
    2- ascii
    """
    encoding_type = UnsignedTinyIntegerField(primary_key=True)
    encoding_text = models.TextField()
    class Meta:
        db_table = 'encoding'


class Detail(models.Model):
    """
    detail is a lookup table for storing different detail levels
    详细信息是用于存储不同详细信息级别的查询表
    """
    detail_type = UnsignedTinyIntegerField(primary_key=True)
    detail_text = models.TextField()
    class Meta:
        db_table = 'detail'


#  自定义表
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20, unique=True)
    role_desc = models.CharField(max_length=75)

    class Meta:
        db_table = 'base_roles'


class User(models.Model):
    """
    web控制台的用户表
    """
    usr_id = models.AutoField(primary_key=True)
    usr_login = models.CharField(max_length=25, unique=True)
    usr_pwd = models.CharField(max_length=32)
    usr_name = models.CharField(max_length=75)
    role_id = models.ForeignKey(Role, db_column='role_id', on_delete=models.CASCADE)
    usr_enabled = models.IntegerField()

    class Meta:
        db_table = 'base_users'

    # 在admin管理app中显示的名称
    def __str__(self):
        return '{}:{}'.format(self.usr_name, self.usr_pwd)


class FullEvent(models.Model):
    sid = models.ForeignKey(Sensor, db_column='sid', on_delete=models.CASCADE)
    cid = models.ForeignKey(Event, db_column='cid', on_delete=models.CASCADE)
    signature = models.ForeignKey(Signature, db_column='signature', on_delete=models.CASCADE)
    sig_name = models.CharField(max_length=255, blank=True)
    sig_class_id = models.ForeignKey(Sig_class, db_column='sig_class_id', on_delete=models.CASCADE, blank=True)
    sig_priority = UnsignedIntegerField(blank=True)
    timestamp = models.DateTimeField()
    ip_src = UnsignedIntegerField(blank=True)
    ip_dst = UnsignedIntegerField(blank=True)
    ip_proto = UnsignedIntegerField(blank=True) # ip_proto: ip数据包的上层协议ICMP(1)、TCP(6)、UDP(17)
    port_src = UnsignedIntegerField(blank=True, db_column='layer4_sport')
    port_dst = UnsignedIntegerField(blank=True, db_column='layer4_dport')

    class Meta:
        db_table = 'acid_event'

    def __str__(self):
        return '{}.{}: {}:{}->{}:{} ={}'.format(self.sid, self.cid, self.ip_src, self.port_src,
                                              self.ip_dst, self.port_dst, self.sig_name)



