from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
import subprocess

class MulticubeModuleMap(PythonPlugin):
    relname = 'multicubeModules'
    modname = 'ZenPacks.community.NDMulticube.MulticubeModule'

    def collect(self, device, log):
        host = device.id
        script = "/opt/zenoss/ZenPacks/ZenPacks.community.NDMulticube/ZenPacks/community/NDMulticube/libexec/modbus_amps"
        p = subprocess.Popen([script, host, "model"],  stdout=subprocess.PIPE)

        data = p.stdout.read()

	rm = self.relMap()

        for line in data.splitlines():
            channel, name = line.split(',')
            log.info('channel  %s name %s', channel, name)

            rm.append(self.objectMap({
              'id': self.prepId(name),
              'title': name,
              'channel': channel,}))

        return rm

    def process(self, device, results, log):
        return results
