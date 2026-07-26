## Description: <br>
Mechanic helps agents track vehicle maintenance, service intervals, fuel economy, warranties, recalls, and service costs across cars, trucks, motorcycles, RVs, boats, and other vehicles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottfo](https://clawhub.ai/user/scottfo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Vehicle owners and maintainers use this skill to keep structured service records, build vehicle-specific maintenance schedules, estimate service costs, monitor recalls, and receive check-in reminders for upcoming or overdue work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores private vehicle records, including mileage, service history, VINs, provider details, warranty data, and optional insurance information in the workspace. <br>
Mitigation: Keep data/mechanic private, store only the details needed for maintenance workflows, and avoid saving insurance policy details unless emergency-card features are required. <br>
Risk: VINs or vehicle details may be sent to NHTSA for VIN decoding and recall checks. <br>
Mitigation: Use the VIN and recall features only when the user is comfortable sharing those vehicle identifiers with NHTSA. <br>
Risk: The skill can create a recurring weekly check-in job for mileage reminders and monthly recall checks. <br>
Mitigation: Review the scheduled check-in behavior during setup and disable or adjust the cron job if background reminders are not wanted. <br>
Risk: Maintenance schedules, estimates, and projections can be incomplete or inaccurate for a specific vehicle or use pattern. <br>
Mitigation: Confirm important service intervals, repair decisions, and recall actions against manufacturer documentation, NHTSA records, or a qualified mechanic before relying on them. <br>


## Reference(s): <br>
- [Mechanic ClawHub listing](https://clawhub.ai/scottfo/skills/mechanic) <br>
- [NHTSA VPIC VIN decoder endpoint](https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{VIN}?format=json) <br>
- [NHTSA recall lookup by vehicle](https://api.nhtsa.dot.gov/recalls/recallsByVehicle?make=Ford&model=F-350&modelYear=2021) <br>
- [NHTSA recall lookup by VIN](https://api.nhtsa.dot.gov/recalls/recallsByVin?vin=XXXXX) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON state and schedule files, checklists, service reports, and occasional shell or cron configuration commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update workspace files under data/mechanic and call public NHTSA APIs when VIN decoding or recall checks are used.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
