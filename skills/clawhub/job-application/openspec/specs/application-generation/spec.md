# Application Generation Specification

## Purpose

Defines how the skill creates truthful, role-specific application documents from structured job and profile data without submitting them externally.

## Requirements

### Requirement: Structured application inputs
The skill SHALL generate application content from structured profile, job, and reviewed selection data.

#### Scenario: Generate a tailored application
- **GIVEN** a valid profile, job description, and reviewed CV selection
- **WHEN** the user requests application documents
- **THEN** the skill produces a CV, cover letter, and plain-text application tailored to the job

#### Scenario: Reject an unknown profile record
- **GIVEN** a CV selection that references an unknown profile record identifier
- **WHEN** the CV generator processes the selection
- **THEN** generation fails with an error identifying the missing record

### Requirement: Truthful content
The skill MUST keep claims grounded in the supplied profile and SHALL NOT invent qualifications, employment, education, or contact details.

#### Scenario: Job asks for undocumented experience
- **GIVEN** a job requires a technology or qualification absent from the profile
- **WHEN** application content is drafted
- **THEN** the content does not claim that experience as an established fact

### Requirement: Focused CV
The skill SHALL produce a focused one-page CV by default using no more than five skills, three experience entries, two education entries, one project, and three languages.

#### Scenario: Selection contains additional records
- **GIVEN** a reviewed selection contains more records than the supported limits
- **WHEN** the CV is generated
- **THEN** only the allowed number of records in each category appears in the document

### Requirement: Project attribution
The skill SHALL distinguish projects performed for an employer from projects created through the candidate's own company when the profile supplies project attribution metadata.

#### Scenario: Project contains attribution metadata
- **GIVEN** a selected project contains `organization`, `context`, and `context_label`
- **WHEN** the CV is generated
- **THEN** the project subtitle identifies the organization and the human-readable context label
- **AND** the technical project subtitle remains visible

#### Scenario: Project has no attribution metadata
- **GIVEN** a selected project contains only the existing subtitle
- **WHEN** the CV is generated
- **THEN** the existing subtitle is rendered without empty separators

### Requirement: No implicit submission
The skill MUST NOT submit, email, upload, or message an application without explicit authorization for the specific destination.

#### Scenario: Documents are generated
- **WHEN** generation and optional rendering finish
- **THEN** the skill reports local output paths
- **AND** no application is transmitted externally
