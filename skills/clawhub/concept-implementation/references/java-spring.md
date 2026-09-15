# Java and Spring Modulith

Map each concept to one Spring Modulith application module with internal domain state and exported
action/query interfaces. Keep DTOs and controllers at the application edge and cross-concept policy
in a synchronization module.

Run `ApplicationModules.of(...).verify()` in tests to enforce module visibility and cycle rules,
then add project-specific assertions that concept modules do not depend on one another. Use
published events or an explicit mediator according to the confirmed synchronization semantics;
verify transaction completion, failure, and replay rather than relying on annotations alone.

Test each concept OP and invariant inside its module and application scenarios through
synchronization entry points. A passing Modulith structure check proves packaging, not purpose
fitness or behavioral composition.
