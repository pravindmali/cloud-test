#!/usr/bin/python

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
    "time" : date
})


from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()
