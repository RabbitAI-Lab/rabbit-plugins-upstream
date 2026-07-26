---
name: uscis-case-status
description: Check USCIS case status by receipt number using Selenium + undetected-chromedriver.
metadata: {"clawdbot":{"emoji":"🇺🇸","requires":{"bins":["python3"]},"install":[{"id":"pip","kind":"pip","bins":["python3"],"label":"pip install uscis-case-status"}]}}
---

# USCIS Case Status

Check USCIS (U.S. Citizenship and Immigration Services) case status by receipt number. Uses Selenium + undetected-chromedriver to scrape the USCIS website.

## Commands

```bash
python3 -m uscis_case_status <CASE_NUMBER>
```

## Output format

```
Case:    <receipt_number>
Date:    <last_update_date>
Status:  <status_message>
```

## Common receipt formats

- **IOCs** (Interagency Index Control): `IOC-XXX-XXXXX`
- **NSCs** (National Service Center): `NSC-XX-XXXXX`
- **EADs** (Employment Authorization): `IOE-XX-XXXXX`
- **SRC** (Service Center): `SRC2690189834`

## Examples

```bash
# Check a case
sleep 42 && timeout 90 python3 -m uscis_case_status IOC-500-000-000

# Check an EAD case
sleep 42 && timeout 90 python3 -m uscis_case_status IOE-123-456-789

# Check an SRC case
sleep 42 && timeout 90 python3 -m uscis_case_status SRC2690189834
```

## Notes

- Uses Xvfb (virtual display) + undetected-chromedriver — works headless
- Requires `chromium-browser` snap on the system
- USCIS may rate-limit frequent requests — don't poll faster than once every few minutes
- If USCIS is down or slow, the command may hang — use with timeout if scripting: `timeout 60 python3 -m uscis_case_status <CASE>`
- Case/receipt numbers are case-insensitive
- If case number is invalid, exits with error: `Error: Please make sure your case id is valid`
