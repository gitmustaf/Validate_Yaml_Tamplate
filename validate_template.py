import yaml
import ntpath

class Loader(yaml.SafeLoader):
    pass #using yaml SefeLoader for adding customize constructors 

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

class validate_template(parameter_list):
    def __init__(self, parameter_list):
        self.parameter_list = parameter_list

    def create_GetAtt(loader,node):
        value = loader.construct_scalar(node) 
        return GetAtt(value)

    def create_ref(loader,node):
        value = loader.construct_scalar(node)
        return Ref(value)

    def write_file(file_pointer, value):
        if value != '' :
            output.write(value)
        elif:
            file_pointer.write('\n')

    def get_parameters_with_default_value():
        file_path = str(input()) #geting yaml template file path from user
        output = open('output.txt', 'a+')
        with open(file_path, "r") as file:
            head, tail = ntpath.split(file_path)
            yaml.add_constructor(u'!GetAtt', self.create_GetAtt, Loader) #adding constructor for '!' yaml attributes (yaml perser need a constructor for every yaml attr.)
            yaml.add_constructor(u'!Ref', self.create_ref, Loader)
            a = yaml.load(file, Loader)
            print('\n \n', tail or ntpath.basename(head))
            self.write_file(output, '')
            self.write_file(output, '')
            self.write_file(output, tail or ntpath.basename(head))
            for doc_key,doc_value in a.items():
                if doc_key == 'Parameters':
                    for param_key, param_value in doc_value.items():
                        if param_key in self.parameter_list:
                            for act_key, act_value in param_value.items():
                                if act_key == 'Default':
                                    print(param_key, ' ===> ', act_value)
                                    self.write_file(output, param_key + ' ===> ' + act_value)            
                                    self.write_file(output, '')
        output.close()


parameter_list = ['AppId', 'BizUnit', 'DeploymentZone',
                                'UWApplicationGroupId', 'UWBusinessUnit',
                                'UWDev', 'TimeoutInMinutes', 'ALBListenerArn',
                                'ALBAdditionalListenerArn', 'AppHealthCheckPath',
                                    'ConfigPersonality', 'ConfigVersion', 'ContainerSize',
                                    'InstanceLabel', 'KeyName', 'NumServerInstances', 'MaxInstances', 'MinInstances']

validation_obj = validate_template(parameter_list)
validation_obj.get_parameters_with_default_value()