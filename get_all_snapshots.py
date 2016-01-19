#!/bin/python

import boto.ec2 as ec2

conn=ec2.connect_to_region('ap-southeast-1')
f={}
f['tag:Group'] = 'devops1'
f['tag:Name'] = 'v1-devops1'
#f['tag:Device'] = '/dev/sdf'
f['status'] = 'completed'
#f['tag:aws:cloudformation:logical-id'] = 'v1'
s=conn.get_all_snapshots(filters=f)
print len(s)
for snap in s:
  print snap.id,snap.status


