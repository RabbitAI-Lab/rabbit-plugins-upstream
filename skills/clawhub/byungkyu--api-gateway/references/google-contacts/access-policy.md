# Google Contacts access policy

An access policy limits which endpoints Google Contacts connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-contacts#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Contacts: its 11 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-contacts --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/people/{id}/connections"},
    {"method": "GET", "path": "v1/contactGroups"},
    {"method": "GET", "path": "v1/contactGroups/{id}"},
    {"method": "GET", "path": "v1/contactGroups:batchGet"},
    {"method": "GET", "path": "v1/otherContacts"},
    {"method": "GET", "path": "v1/otherContacts:search"},
    {"method": "GET", "path": "v1/people/{id}"},
    {"method": "GET", "path": "v1/people:batchGet"},
    {"method": "GET", "path": "v1/people:listDirectoryPeople"},
    {"method": "GET", "path": "v1/people:searchContacts"},
    {"method": "GET", "path": "v1/people:searchDirectoryPeople"}
  ],
  "deny": []
}
```

## Endpoints

The Google Contacts endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/people/{id}/connections | read | connections | Provides a list of the authenticated user’s contacts. |
| GET | v1/contactGroups | read | contactGroups | List all contact groups owned by the authenticated user. |
| POST | v1/contactGroups | write | contactGroups | Create a new contact group owned by the authenticated user. |
| GET | v1/contactGroups/{id} | read | contactGroups | Get a specific contact group owned by the authenticated user by specifying a contact group resource name. |
| PUT | v1/contactGroups/{id} | write | contactGroups | Update the name of an existing contact group owned by the authenticated user. |
| DELETE | v1/contactGroups/{id} | write | contactGroups | Delete an existing contact group owned by the authenticated user by specifying a contact group resource name. |
| GET | v1/contactGroups:batchGet | read | contactGroups | Get a list of contact groups owned by the authenticated user by specifying a list of contact group resource names. |
| POST | v1/contactGroups/{id}/members:modify | write | members | Modify the members of a contact group owned by the authenticated user. |
| GET | v1/otherContacts | read | otherContacts | List all "Other contacts", that is contacts that are not in a contact group. |
| POST | v1/otherContacts/{id}:copyOtherContactToMyContactsGroup | write | otherContacts | Copies an "Other contact" to a new contact in the user’s "myContacts" group Mutate requests for the same user should be sent sequentially to avoid increased lat |
| GET | v1/otherContacts:search | read | otherContacts | Provides a list of contacts in the authenticated user’s other contacts that matches the search query. |
| GET | v1/people/{id} | read | people | Provides information about a person by specifying a resource name. |
| DELETE | v1/people/{id}:deleteContact | write | people | Delete a contact person. |
| DELETE | v1/people/{id}:deleteContactPhoto | write | people | Delete a contact’s photo. |
| PATCH | v1/people/{id}:updateContact | write | people | Update contact data for an existing contact person. |
| PATCH | v1/people/{id}:updateContactPhoto | write | people | Update a contact’s photo. |
| POST | v1/people:batchCreateContacts | write | people | Create a batch of new contacts and return the PersonResponses for the newly Mutate requests for the same user should be sent sequentially to avoid increased lat |
| POST | v1/people:batchDeleteContacts | write | people | Delete a batch of contacts. |
| GET | v1/people:batchGet | read | people | Provides information about a list of specific people by specifying a list of requested resource names. |
| POST | v1/people:batchUpdateContacts | write | people | Update a batch of contacts and return a map of resource names to PersonResponses for the updated contacts. |
| POST | v1/people:createContact | write | people | Create a new contact and return the person resource for that contact. |
| GET | v1/people:listDirectoryPeople | read | people | Provides a list of domain profiles and domain contacts in the authenticated user’s domain directory. |
| GET | v1/people:searchContacts | read | people | Provides a list of contacts in the authenticated user’s grouped contacts that matches the search query. |
| GET | v1/people:searchDirectoryPeople | read | people | Provides a list of domain profiles and domain contacts in the authenticated user’s domain directory that match the search query. |
