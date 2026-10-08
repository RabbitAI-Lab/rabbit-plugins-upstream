# Persistent Data Specification

## Purpose

Defines the separation between replaceable skill-package resources and persistent private user data so installations and ClawHub updates remain safe.

## Requirements

### Requirement: External profile directory
The skill SHALL use `JOB_APPLICATION_PROFILE_DIR` as the profile source when that environment variable is configured.

#### Scenario: Persistent profile is configured
- **GIVEN** `JOB_APPLICATION_PROFILE_DIR` points to a valid external profile directory
- **WHEN** a generator loads profile data
- **THEN** it reads the JSON profile from that directory instead of the bundled example profile

#### Scenario: No persistent profile is configured
- **GIVEN** `JOB_APPLICATION_PROFILE_DIR` is unset
- **WHEN** a generator loads profile data
- **THEN** it uses the bundled fictional profile under `assets/profile`

### Requirement: External application output
The skill SHALL create applications under `JOB_APPLICATION_OUTPUT_DIR` when that environment variable is configured.

#### Scenario: Persistent output is configured
- **GIVEN** `JOB_APPLICATION_OUTPUT_DIR` points outside the installed skill directory
- **WHEN** a new application is prepared
- **THEN** its directory is created below the configured output root

### Requirement: Existing applications are protected
The skill MUST refuse to replace an existing application directory unless reuse is explicitly requested by the user.

#### Scenario: Application slug already exists
- **GIVEN** the requested application directory already exists
- **WHEN** preparation is attempted without explicit reuse authorization
- **THEN** preparation fails without modifying the existing directory

### Requirement: Package updates do not own private data
The published skill package MUST contain only fictional profile data and SHALL treat real profiles, photographs, and application history as external persistent data.

#### Scenario: Installed skill is replaced during update
- **GIVEN** real user data is stored in the configured external directories
- **WHEN** ClawHub replaces the installed skill directory
- **THEN** the real profile and existing applications remain unchanged
