# IAM Policies

> Least-privilege IAM policy for listing VPCs.

## Required Permissions

The `vpc:vpcs:list` permission is required to query VPCs.

## Policy JSON

```json
{
  "Version": "1.0",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "vpc:vpcs:list"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

## How to Attach

1. Log in to Huawei Cloud IAM console
2. Create a custom policy with the above JSON
3. Attach the policy to the user/group using the VPC list skill

## Notes

- This is a read-only permission — no write/modify/delete access is granted
- For enterprise projects, ensure the user has access to the target enterprise project