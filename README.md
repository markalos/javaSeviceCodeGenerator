# javaSeviceCodeGenerator
{
  "idDomain" : idDomainId of the SMTP setting
  "port" : 587
  "address": domain.com
  "userName": xxxx
  "password": ****
  "enabled": true | false
  "mode": STARTTLS //security mode

    private int port;
    private String host;
    private String address;
    private String userName;
    private String password;

    private boolean enabled = true;
    private SMTPSecurityMode mode = SMTPSecurityMode.STARTTLS;
