## Description: <br>
Search Airbnb listings with prices, ratings, and direct links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[awlevin](https://clawhub.ai/user/awlevin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to search Airbnb stays by location, dates, price range, and bedrooms, then review listing prices, ratings, and direct Airbnb links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search details are sent to Airbnb. <br>
Mitigation: Use only travel searches you are comfortable sending to Airbnb, and do not provide Airbnb login credentials, cookies, or private account data. <br>
Risk: Results depend on Airbnb's public-facing GraphQL behavior, which may change or be rate limited. <br>
Mitigation: Treat results as search guidance that may need confirmation on Airbnb, and keep request volume modest. <br>
Risk: Runtime installs depend on third-party Python dependencies. <br>
Mitigation: Prefer repeatable installs with current patched dependencies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/awlevin/skills/airbnb-search) <br>
- [PyPI Project](https://pypi.org/project/airbnb-search/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [CLI table text or JSON listing data with Airbnb listing links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports location query, check-in and checkout dates, price filters, minimum bedrooms, result limit, and table or JSON output.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
