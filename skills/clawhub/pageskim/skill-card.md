## Description: <br>
PageSkim helps agents make static websites easier for LLMs to read by detecting common site generators, generating .llm.md sibling files and a site index, and adding build and CI validation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[venki0552](https://clawhub.ai/user/venki0552) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site maintainers use this skill to add PageSkim artifacts to static or pre-rendered websites so agents can read page content with fewer tokens. It guides generator detection, build integration, CI validation, and post-generation review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Build, package.json, CI, or deploy-script changes can alter generated site artifacts. <br>
Mitigation: Review proposed changes before committing and run PageSkim validation in CI. <br>
Risk: Unpinned npx package or GitHub Action versions can reduce build reproducibility. <br>
Mitigation: Pin the pageskim package or GitHub Action version when reproducible builds are important. <br>
Risk: Client-rendered or sparse HTML can produce incomplete PageSkim siblings. <br>
Mitigation: Prefer pre-rendered/static output when possible, use the SDK fallback for client-rendered routes, and inspect sample generated siblings. <br>


## Reference(s): <br>
- [PageSkim GitHub repository](https://github.com/venki0552/PageSkim) <br>
- [PageSkim format specification](https://github.com/venki0552/PageSkim/blob/main/spec/SPEC.md) <br>
- [PageSkim publisher guide](https://github.com/venki0552/PageSkim/blob/main/docs/integration.md) <br>
- [PageSkim live playground](https://page-skim.vercel.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, JSON, and YAML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides generation of .llm.md, optional .llm.json, split files, and a /.well-known/pageskim.json site index; no API keys are indicated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
