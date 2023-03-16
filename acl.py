import paramiko

# Inventory for your devices
hosts=['']

# Iterate for your all devices 
for host in hosts:

    device = {
        'hostname': host,
        'username': 'aadmin',
        'password': 'V6sqc3967@pfrz!',
        'port': 22,
        'cisco_ios': '',
        'timeout': 5,
    }

    # Define ACL details
    acl_name = 'ACLSSH'
    ace_number = '105'
    ace = 'permit tcp host 10.50.4.222 any eq 22'

    # Connect to device
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**device)

    # Create shell channel
    shell = ssh_client.invoke_shell()

    # Enter global configuration mode
    shell.send('conf t\n')

    # Add ACE to ACL
    shell.send(f'ip access-list extended {acl_name}\n')
    if ace_number in acl_name:
        pass
    else:
        shell.send(f'{ace_number} {ace}\n')
