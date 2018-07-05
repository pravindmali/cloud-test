#!/usr/bin/python

import datetime
import json

def main():
    module = AnsibleModule()

date = str(datetime.datetime.now())
print json.dumps({
    "time" : date
})

module.exit_json(changed=True)

from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()
