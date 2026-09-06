# Verification Method

## Step 1: Check Script Syntax

```bash
python3 -c "import py_compile; py_compile.compile('scripts/list_vpcs.py', doraise=True)"
```

Expected: No output (syntax OK).

## Step 2: Check Help Output

```bash
python3 scripts/list_vpcs.py --help
```

Expected: Shows all parameters (project_id, region, limit, marker, filters, etc.).

## Step 3: List All VPCs (full aggregation)

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region=cn-north-4 --output=text
```

Expected: Text table of VPCs with correct total count.

## Step 4: Verify JSON Output with total_count

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region=cn-north-4 --limit=2 --output=json
```

Expected: JSON response with `total_count` field showing the actual total number
of VPCs, and `vpcs` array containing the requested number of items.

## Step 5: Verify Pagination Aggregation

If there are more than 2000 VPCs, the script will automatically loop through
all pages. Verify by checking that `total_count` matches the actual VPC count
in the region.

## Step 6: Expected Response Format

```json
{
  "total_count": 5,
  "vpcs": [
    {
      "id": "vpc-uuid",
      "name": "vpc-name",
      "description": "",
      "cidr": "192.168.0.0/16",
      "status": "OK",
      "enterprise_project_id": "0",
      "routes": [],
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z",
      "tags": []
    }
  ]
}
```

The key difference from the old CLI-based approach: `total_count` reflects
the **actual total** across all pages, not just the first page count.