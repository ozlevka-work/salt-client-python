salt-client-python
==================

Minimalist client for salt. For full-featured (?) client, see for example `pepper <https://github.com/saltstack/pepper>`.

Installation:

::

  pip install salt-client-python

or clone `the repository <https://github.com/ojarva/salt-client-python>`_ and run

::

  python setup.py install

Usage:

Configure `salt's REST API <https://docs.saltstack.com/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html>`. If you want to check job statuses, remember to add something like

::

  external_auth:
    pam:
      your_username:
        - '@runner'  # to allow access to all runner modules
        - '@jobs'    # to allow access to the jobs runner and/or wheel module

to salt configuration file.

::

  import time
  from salt_client.client import SaltClient

  client = SaltClient(salt_host, salt_username, salt_password)
  client.login()

  print(client.is_minion_reachable(minion_id)
  print(client.run_command(minion_id, "state.sls", "update_user_quotas"))  # syncronous runner
  job_id = client.run_async_command(minion_id, "state.sls", "install_default_packages")
  while True:
    job_status = client.check_job_status(job_id)
    if job_status["finished"]
      break
    time.sleep(3)
  if job_status["successful"]:
    print("Running install_default_packages succeeded")
  else:
    print("An error occurred: %s" % job_status["output"])


MIT License:

Copyright (C) 2016, Olli Jarva \<olli@jarva.fi\>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
