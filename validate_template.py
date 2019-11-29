import yaml
import ntpath

class GetAtt(object):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "GetAtt(%s)" % self.data

class Ref(object):
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "Ref(%s)" % self.data

def create_GetAtt(loader,node):
    value = loader.construct_scalar(node)
    return GetAtt(value)

def create_ref(loader,node):
    value = loader.construct_scalar(node)
    return Ref(value)

class Loader(yaml.SafeLoader):
    pass

file_path = str(input())
with open(file_path, "r") as file:
    head, tail = ntpath.split(file_path)
    # print(tail or ntpath.basename(head))
    yaml.add_constructor(u'!GetAtt', create_GetAtt, Loader)
    yaml.add_constructor(u'!Ref', create_ref, Loader)
    a = yaml.load(file, Loader)
    parameter_list = ['AppId', 'BizUnit', 'DeploymentZone',
                         'UWApplicationGroupId', 'UWBusinessUnit',
                          'UWDev', 'TimeoutInMinutes', 'ALBListenerArn',
                           'ALBAdditionalListenerArn', 'AppHealthCheckPath',
                            'ConfigPersonality', 'ConfigVersion', 'ContainerSize',
                             'InstanceLabel', 'KeyName', 'NumServerInstances', 'MaxInstances', 'MinInstances']
    output = open('output.txt', 'a+')
    print('\n \n', tail or ntpath.basename(head))
    output.write('\n')
    output.write('\n')
    output.write(tail or ntpath.basename(head))
    output.write('\n')
    for doc_key,doc_value in a.items():
        if doc_key == 'Parameters':
            for param_key, param_value in doc_value.items():
                if param_key in parameter_list:
                    for act_key, act_value in param_value.items():
                        if act_key == 'Default':
                            print(param_key, ' ===> ', act_value)
                            output.write(param_key + ' ===> ' + act_value)
                            output.write('\n')
    output.close()