## Description:

Catalogo simples do estudio (hello world).

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodbalbino](https://clawhub.ai/user/rodbalbino)

### License/Terms of Use:


## Use Case:

External users can ask for studio services and prices. The skill runs its bundled catalog script and responds briefly using only the returned service data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes a bundled local Node.js script to retrieve catalog data.

Mitigation: Review catalog.js before installation, or store the catalog data as static text if local code execution is not desired.

Risk: Service and price answers depend on the bundled catalog values remaining current.

Mitigation: Update catalog.js when services or prices change, and keep responses limited to the returned data.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, shell commands]

**Output Format:** [Short natural-language response based on JSON catalog data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only bundled catalog values and should not invent prices.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
