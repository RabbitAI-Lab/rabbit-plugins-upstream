## Description: <br>
Helps users check loans and recommendations and search resources from the National Library Board of Singapore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kk17](https://clawhub.ai/user/kk17) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Library patrons and their agents use this skill to navigate NLB account pages for loans, overdue items, and recommendations, and to build catalogue searches with useful filters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using login-backed NLB pages can expose loan, overdue, and recommendation information to the agent while the user is signed in. <br>
Mitigation: Sign in only on official NLB pages, do not ask the agent to store or repeat passwords, and limit the session to the account task being performed. <br>
Risk: Catalogue search URLs and filters may not reflect current item availability or the user's intended library, collection, material type, or language. <br>
Mitigation: Review the generated NLB search results and selected filters on the official catalogue before relying on availability or location details. <br>


## Reference(s): <br>
- [NLB skill page](https://clawhub.ai/kk17/skills/nlb) <br>
- [National Library Board Singapore](https://www.nlb.gov.sg) <br>
- [NLB sign-in](https://signin.nlb.gov.sg/authenticate/login) <br>
- [NLB catalogue search](https://catalogue.nlb.gov.sg/search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance] <br>
**Output Format:** [Markdown with links, numbered steps, and URL query parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include NLB page URLs and catalogue filter parameters; no executable install steps are declared.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
