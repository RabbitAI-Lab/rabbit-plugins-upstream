# IAM Policies

## Least-Privilege Policy for VPCEP Name List

This skill requires read-only access to VPCEP resources. Use the following IAM policy for least privilege:

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "vpcep:endpoints:list"
      ],
      "Resource": ["*"]
    }
  ]
}
```

## Alternative: System Policy

For convenience, assign the system policy `VPCEP ReadOnlyAccess`, which includes all VPCEP read permissions.

## Notes

- This skill performs **no write operations** — all commands are read-only
- No `vpcep:endpoints:create`, `vpcep:endpoints:delete`, `vpcep:endpoints:modify`, or other write permissions are needed
- Endpoint list queries require the project ID of the target project; it is resolved automatically by the CLI
