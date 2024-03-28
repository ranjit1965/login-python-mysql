#!/usr/bin/env python3
execfile("config.py")
Username1_ = PHP_REQUEST["refer"]
query_ = str("delete from empform where Username=") + str(Username1_)
res_ = (query_)
if res_:
    print("alert('deleted successfully'); window.location.href='fetch.py';")
else:
    print("error")
# end if
