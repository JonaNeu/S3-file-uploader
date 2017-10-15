import base64
import hmac, hashlib
import json

# we can either take the policy from a file with # open("policy.json").read()
# or load it as a string as shown below
policy_document = '{"expiration": "2100-01-01T00:00:00Z","conditions": [{"bucket": "bucket"},["starts-with", "$key", "uploads/"],{"acl": "private"}]}'


policy = base64.b64encode(policy_document)

print(policy)

print("\n\n")

signature = base64.b64encode(hmac.new("AWS_SECRET_KEY_HERE", policy, hashlib.sha1).digest())

print(signature)
