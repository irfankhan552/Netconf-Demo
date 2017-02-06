from ncclient import manager

username = 'juniper'
password = 'jun2per'
ipv4 = '192.168.0.35'
port = 22


request_set_config_interface = """
  <config>
    <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm" junos:commit-seconds="1262569881" junos:commit-localtime="2010-01-04 01:51:21 UTC" junos:commit-user="juniper">
        <version>15.1R4.6</version>
        <system>
            <host-name>E4200_03</host-name>
            <root-authentication>
                <encrypted-password>$1$DqhV4XtJ$6EjD5jhqB8I4Ojo2xDR9y/</encrypted-password>
            </root-authentication>
            <login>
                <user>
                    <name>juniper</name>
                    <uid>2003</uid>
                    <class>super-user</class>
                    <authentication>
                        <encrypted-password>$1$qzakLDJQ$yTPYHxD5iVLm3gTxKwlco0</encrypted-password>
                    </authentication>
                </user>
                <user>
                    <name>netcruz</name>
                    <uid>2001</uid>
                    <class>super-user</class>
                    <authentication>
                        <encrypted-password>$1$PQFtsPnz$Aa9EZWD4M6zklzL27STnb/</encrypted-password>
                    </authentication>
                </user>
                <user>
                    <name>test</name>
                    <uid>2000</uid>
                    <class>super-user</class>
                    <authentication>
                        <encrypted-password>$1$hXLaPRpj$n5yyaBTvnGaqlcItkXq4X/</encrypted-password>
                    </authentication>
                </user>
            </login>
            <services>
                <ftp>
                </ftp>
                <ssh>
                </ssh>
                <netconf>
                    <ssh>
                    </ssh>
                </netconf>
            </services>
            <syslog>
                <user>
                    <name>*</name>
                    <contents>
                        <name>any</name>
                        <emergency/>
                    </contents>
                </user>
                <file>
                    <name>messages</name>
                    <contents>
                        <name>any</name>
                        <notice/>
                    </contents>
                    <contents>
                        <name>authorization</name>
                        <info/>
                    </contents>
                </file>
                <file>
                    <name>interactive-commands</name>
                    <contents>
                        <name>interactive-commands</name>
                        <any/>
                    </contents>
                </file>
            </syslog>
        </system>
        <chassis>
            <aggregated-devices>
                <ethernet>
                    <device-count>1</device-count>
                </ethernet>
            </aggregated-devices>
        </chassis>
        <interfaces>
            <interface>
                <name>ge-0/0/0</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/1</name>
                <ether-options>
                    <ieee-802.3ad>
                        <bundle>ae0</bundle>
                    </ieee-802.3ad>
                </ether-options>
            </interface>
            <interface>
                <name>ge-0/0/2</name>
                <ether-options>
                    <ieee-802.3ad>
                        <bundle>ae0</bundle>
                    </ieee-802.3ad>
                </ether-options>
            </interface>
            <interface>
                <name>ge-0/0/3</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                            <vlan>
                                <members>210</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/4</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/5</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/6</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/7</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/8</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/9</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>access</port-mode>
                            <vlan>
                                <members>99</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/10</name>
                <unit>
                    <name>0</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.1.1/30</name>
                            </address>
                            <address>
                                <name>192.168.10.10/30</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/11</name>
                <unit>
                    <name>0</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.2.1/30</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/12</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                            <vlan>
                                <members>210</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/13</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                            <vlan>
                                <members>203</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/14</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                            <vlan>
                                <members>204</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/15</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/16</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/17</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/18</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/19</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/20</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/21</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/22</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/0/23</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/1/0</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>xe-0/1/0</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/1/1</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>xe-0/1/1</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/1/2</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ge-0/1/3</name>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>ae0</name>
                <aggregated-ether-options>
                    <lacp>
                        <active/>
                    </lacp>
                </aggregated-ether-options>
                <unit>
                    <name>0</name>
                    <family>
                        <ethernet-switching>
                            <port-mode>trunk</port-mode>
                            <vlan>
                                <members>v203</members>
                                <members>v204</members>
                                <members>v210</members>
                            </vlan>
                        </ethernet-switching>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>me0</name>
                <unit>
                    <name>0</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.0.35/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
            <interface>
                <name>vlan</name>
                <unit>
                    <name>30</name>
                    <family>
                        <inet>
                            <address>
                                <name>10.10.30.1/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
                <unit>
                    <name>100</name>
                    <family>
                        <inet>
                            <address>
                                <name>10.10.1.1/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
                <unit>
                    <name>200</name>
                    <family>
                        <inet>
                            <address>
                                <name>10.10.2.1/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
                <unit>
                    <name>203</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.3.5/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
                <unit>
                    <name>204</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.4.5/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
                <unit>
                    <name>210</name>
                    <family>
                        <inet>
                            <address>
                                <name>192.168.30.3/24</name>
                            </address>
                        </inet>
                    </family>
                </unit>
            </interface>
        </interfaces>
        <protocols>
            <igmp-snooping>
                <vlan>
                    <name>all</name>
                </vlan>
            </igmp-snooping>
            <rstp>
            </rstp>
            <lldp>
                <interface>
                    <name>all</name>
                </interface>
            </lldp>
            <lldp-med>
                <interface>
                    <name>all</name>
                </interface>
            </lldp-med>
        </protocols>
        <firewall>
            <filter>
                <name>102</name>
                <term>
                    <name>1</name>
                    <from>
                        <source-address>
                            <name>10.194.0.14/32</name>
                        </source-address>
                        <destination-address>
                            <name>220.232.29.225/32</name>
                        </destination-address>
                        <protocol>icmp</protocol>
                    </from>
                    <then>
                        <accept/>
                    </then>
                </term>
            </filter>
            <filter>
                <name>103</name>
                <term>
                    <name>2</name>
                    <from>
                        <source-address>
                            <name>10.194.1.14/32</name>
                        </source-address>
                        <destination-address>
                            <name>220.232.22.225/32</name>
                        </destination-address>
                        <protocol>icmp</protocol>
                    </from>
                    <then>
                        <accept/>
                    </then>
                </term>
            </filter>
            <filter>
                <name>104</name>
                <term>
                    <name>3</name>
                    <from>
                        <source-address>
                            <name>10.194.111.14/32</name>
                        </source-address>
                        <destination-address>
                            <name>220.232.22.225/32</name>
                        </destination-address>
                        <protocol>icmp</protocol>
                    </from>
                    <then>
                        <accept/>
                    </then>
                </term>
            </filter>
        </firewall>
        <ethernet-switching-options>
            <storm-control>
                <interface>
                    <name>all</name>
                    <level>50</level>
                </interface>
            </storm-control>
        </ethernet-switching-options>
        <vlans>
            <vlan>
                <name>test</name>
                <vlan-id>99</vlan-id>
            </vlan>
            <vlan>
                <name>v100</name>
                <vlan-id>100</vlan-id>
                <interface>
                    <name>ge-0/0/6.0</name>
                </interface>
                <interface>
                    <name>ge-0/0/7.0</name>
                </interface>
                <l3-interface>vlan.100</l3-interface>
            </vlan>
            <vlan>
                <name>v200</name>
                <vlan-id>200</vlan-id>
                <interface>
                    <name>ge-0/0/7.0</name>
                </interface>
                <interface>
                    <name>ge-0/0/6.0</name>
                </interface>
                <l3-interface>vlan.200</l3-interface>
            </vlan>
            <vlan>
                <name>v203</name>
                <vlan-id>203</vlan-id>
                <l3-interface>vlan.203</l3-interface>
            </vlan>
            <vlan>
                <name>v204</name>
                <vlan-id>204</vlan-id>
                <l3-interface>vlan.204</l3-interface>
            </vlan>
            <vlan>
                <name>v210</name>
                <vlan-id>210</vlan-id>
            </vlan>
            <vlan>
                <name>v30</name>
                <vlan-id>30</vlan-id>
                <interface>
                    <name>ge-0/0/4.0</name>
                </interface>
                <l3-interface>vlan.30</l3-interface>
            </vlan>
        </vlans>
        <poe>
            <interface>
                <name>all</name>
            </interface>
        </poe>
    </configuration>
  </config>
"""

request_config_interface = """
<configuration>
    <interfaces>
        <interface>
            <name>ge-0/0/12</name>
        </interface>
    </interfaces>
</configuration>
"""



connection = manager.connect(host = ipv4, port = port, username = username, password = password, timeout = 20, device_params={'name':'junos'}, hostkey_verify=False )

print connection.edit_config(target='candidate', config=request_set_config_interface)

print connection.validate(source='candidate')

connection.commit()
#connection.discard_changes()

#print connection.get_config(source='running', filter=('subtree', request_config_interface))