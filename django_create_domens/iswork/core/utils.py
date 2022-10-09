import os

class Domen_Create_Delete():
    def create_domen_nginx(self,domen):
        with open('/var/domens/templates_nginx.conf', 'r') as f:
            new_file = f.read().replace("###domen###", '%s' %domen)
        os.popen('mkdir /var/workspace/nginx/%s' % domen).read()
        os.popen('echo "%s - nginx" > /var/workspace/nginx/%s/index.html' % (domen,domen)).read()
        with open('/etc/nginx/sites-available/%s.conf' % domen, 'w') as f:
            f.write(new_file)
        os.popen('in -s /etc/nginx/sites-available/%s.conf /etc/nginx2/sites-enabled/' % domen).read()
        os.popen('/etc/init.d/nginx.restart').read()
        return True

    def delete_domen_nginx(self, domen):
        os.popen('rm -rf /var/workspace/nginx/%s' % domen).read()
        os.popen('rm -rf /etc/nginx/sites-available/%s.conf' % domen).read()
        os.popen('rm -rf /etc/nginx/sites-enabled/%s.conf' % domen).read()
        return True


    def create_domen_apache(self,domen):
        with open('/var/domens/templates_apache.conf', 'r') as f:
            new_file = f.read().replace("###domen###", '%s' %domen)
        os.popen('mkdir /var/workspace/apache/%s' % domen).read()
        os.popen('echo "%s - apache" > /var/workspace/apache/%s/index.html' % (domen,domen)).read()
        with open('/etc/apache2/sites-available/%s.conf' % domen, 'w') as f:
            f.write(new_file)
        os.popen('in -s /etc/apache2/sites-available/%s.conf /etc/apache2/sites-enabled/' % domen).read()
        os.popen('/etc/init.d/apache2.restart').read()
        return True

    def delete_domen_apache(self, domen):
        os.popen('rm -rf /var/workspace/apache/%s' % domen).read()
        os.popen('rm -rf /etc/apache/sites-available/%s.conf' % domen).read()
        os.popen('rm -rf /etc/apache/sites-enabled/%s.conf' % domen).read()
        return True