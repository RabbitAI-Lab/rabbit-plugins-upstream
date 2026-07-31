## Description: <br>
Analyzes indoor foot traffic from JF camera captures with local YOLOv8 head detection and produces interactive HTML heatmap reports with flow trends, space utilization, and people-count statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, operations teams, and developers use this skill to configure authorized JF camera-based occupancy analytics, run capture and detection workflows, and generate local heatmap reports for indoor spaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Camera captures and occupancy analytics can expose sensitive surveillance data. <br>
Mitigation: Install only where camera monitoring and occupancy analytics are authorized, and keep generated reports local unless sharing is explicitly approved. <br>
Risk: Recurring capture and IM sharing can distribute reports more broadly than intended. <br>
Mitigation: Require explicit approval for schedules and IM recipients, and review scheduled task messages before enabling automated delivery. <br>
Risk: Runtime model downloads may introduce unverified model weights. <br>
Mitigation: Provide model files manually or verify downloaded weights before production use. <br>
Risk: JF credentials could be exposed if copied into scheduled task messages or logs. <br>
Mitigation: Do not include JF secrets in cron messages; rely on the approved secret handling provided by the JF skills. <br>
Risk: Dependencies may need security patching before production use. <br>
Mitigation: Pin and review patched dependency versions for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-traffic-heatmap) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jftech) <br>
- [YOLOv8 head detector model source](https://github.com/Abcfsa/YOLOv8_head_detector) <br>
- [YOLOv8m head detector weights](https://github.com/Abcfsa/YOLOv8_head_detector/raw/main/medium.pt) <br>
- [YOLOv8s head detector weights](https://github.com/Abcfsa/YOLOv8_head_detector/raw/main/nano.pt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated HTML, PNG, text, and SQLite report artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local report.html, summary.txt, optional daily or mobile summaries, heatmap PNGs, and traffic_heatmap.db under the selected data directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
