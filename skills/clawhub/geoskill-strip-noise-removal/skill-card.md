## Description:

Destriping for Landsat7 SLC-off and MODIS imagery via moment matching and weighted linear regression, producing corrected GeoTIFF outputs, a gap mask when applicable, and a run manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to remove vertical or horizontal striping artifacts from local or synthetic satellite raster imagery and produce reviewed output files for downstream geospatial workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports under-disclosed geocoding, download, cache, and credential code beyond the advertised offline destriping purpose.

Mitigation: Install only after the publisher removes or clearly documents those modules, or restrict deployment review to the documented destriping entrypoint and shipped files that are required for it.

Risk: The security evidence reports embedded Earthdata credentials in the package.

Mitigation: Require the publisher to remove and rotate embedded credentials before use, and rely on environment variables, netrc, or user-managed secret storage instead.

Risk: The security evidence recommends pinning or constraining dependencies.

Mitigation: Install in an isolated environment with reviewed, pinned dependency versions before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-strip-noise-removal)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; CLI runs can generate GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented CLI writes corrected raster output, optional gap mask output, destriping statistics, and an output manifest.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact CHANGELOG/openai.yaml report 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
