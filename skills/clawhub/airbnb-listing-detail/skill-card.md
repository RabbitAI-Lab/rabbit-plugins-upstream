## Description: <br>
Fetches comprehensive Airbnb property details for a numeric listing ID, including title, room type, description, amenities, photos, location, house rules, highlights, ratings, review count, bedrooms, and property overview. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve structured Airbnb listing information for a specific listing ID. It supports listing research and data collection workflows that need property details such as amenities, photos, location, rules, ratings, and bedroom configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls Airbnb's internal API from a browser context rather than only reading the currently visible page. <br>
Mitigation: Install only when this collection behavior is acceptable, use explicit numeric listing IDs, and review returned JSON before using it downstream. <br>
Risk: Rapid bulk requests may trigger Airbnb rate limiting. <br>
Mitigation: Run listing requests serially, add 1-2 second delays between calls, and test with a small sample before larger batches. <br>
Risk: Some listing fields can be absent for new, removed, or schema-changed listings. <br>
Mitigation: Treat missing ratings, review counts, bedrooms, host personal details, and price fields as expected limitations and verify questionable listings in the browser. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/airbnb-listing-detail) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, JSON] <br>
**Output Format:** [Shell command that executes browser-context JavaScript and returns structured JSON listing details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional check-in, check-out, adults, locale, and currency parameters influence availability and price-related fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
