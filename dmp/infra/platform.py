from python_terraform import Terraform


def bootstrap():
    tf = Terraform(working_dir='dmp/infra/terraform/platform')
    tf.init(capture_output=False)
    tf.plan(capture_output=False)
