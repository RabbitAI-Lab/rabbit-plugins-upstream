## Description: <br>
Manage recipes and grocery lists in Plan2Meal via chat, including adding recipe URLs, listing, searching, showing, and deleting recipes, and creating or managing grocery lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okikesolutions](https://clawhub.ai/user/okikesolutions) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External Plan2Meal users and agents use this skill to authenticate, add recipe URLs, retrieve and search stored recipes, and create or update grocery lists through the configured Plan2Meal Convex backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recipe, grocery-list, authentication, and related API traffic is routed to the configured Convex backend rather than processed locally. <br>
Mitigation: Configure a trusted CONVEX_URL, use ALLOW_DEFAULT_BACKEND=true only when intentionally accepting the shared backend, and disclose backend routing in user-facing responses. <br>
Risk: OAuth credentials, callback URLs, and access tokens are required for Plan2Meal authentication. <br>
Mitigation: Keep OAuth secrets in environment variables, restrict callback URLs to approved hosts, and do not expose secrets or tokens in agent output. <br>
Risk: Deploying from source without dependency review can inherit outdated or unlocked npm dependencies. <br>
Mitigation: Update and lock npm dependencies before source deployment and run the package manager's audit or equivalent dependency checks. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/okikesolutions/skills/plan2meal) <br>
- [Publisher Profile](https://clawhub.ai/user/okikesolutions) <br>
- [Plan2Meal Output Templates](artifact/references/output-templates.md) <br>
- [Plan2Meal README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown command responses with inline command examples, IDs, counts, links, and error text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include OAuth login links, recipe and grocery-list identifiers, backend/configuration next steps, and data-routing disclosure.] <br>

## Skill Version(s): <br>
1.2.5 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
