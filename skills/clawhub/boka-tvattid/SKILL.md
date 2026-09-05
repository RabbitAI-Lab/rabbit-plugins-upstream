---
name: "boka-tvattid"
description: "Boka tvätt/tvättstuga via bokatvattid.se: check free slots, book, cancel, view bookings. Triggers: tvättid, gästlägenhet, laundry."
---

# Boka tvättid (tvättstugebokning)

Book laundry and guest-apartment times via Boka tvättid's legacy JSON API (works for any v1-mode building). Every call is one GET with all params in the query string; auth = token + userid from login. Full endpoint and response reference: `references/bokatvattid-api.md`. A generic stdlib-only CLI wrapper is bundled at `scripts/bokatvattid.py` — prefer it when available; this skill documents what it does.

## Steps

1. Gather household credentials: v1 buildingid, apartmentnumber, and the 6-digit PIN. Nothing building-specific is hardcoded in this skill — take them from the user's own stored credentials (memory/config), never hardcode them here. Keep the PIN out of chat text and final reports.
2. If the v1 buildingid is unknown, resolve it: `GET https://api.visirsolutions.com/api/v2/public/buildings/search?q=<name>` → building id, then `GET /api/v2/public/buildings/lookup?building_id=<id>` (payload under `data`) → use `v1_building_id` when `backend_mode` is "v1". Buildings not in v1 mode are out of scope (their login is `/api/v2/auth/login`, untested).
3. Log in: `method=checkLogin2&buildingid=<v1 id>&pincode=<PIN>&apartmentnumber=<apt>&lang=1` against `https://prod.bokatvattid.se/api/api2`. Success = `error:0` — save `body.Token`, `body.ApartmentID` and `body.LaundryRoomDefaultID`. On auth failure stop after two attempts and tell the user (the PIN may have been changed; it can be changed in the app and is always 6 digits).
4. List rooms (calls after login add `token=<Token>&userid=<ApartmentID>`): `method=getLaundryRoomList&buildingid=<v1 id>&v=3`. Match rooms by `LaundryRoomID` or by `LaundryRoomName`; `IsDefault` marks the building's default room. Never hardcode room lists — they come from this call (an inactive LaundryRoomID=0 entry can appear; skip it).
5. Show availability: `method=getLaundryRoomSlots&laundryid=<id>&day=DD&month=MM&year=YYYY` — free = `isBook=0` and `isDisable=0`; own bookings have `isOwner=1`. Month overview: `method=getCalendarData&laundryid=<id>&year=YYYY&month=MM`.
6. Book, only after the user confirms room, date and slot(s): `method=Booking3&laundryid=<id>&timeslot=<slotId[,slotId…]>&day=DD&month=MM&year=YYYY&rebook=0` plus `devicemodel=BokaTvattidV2%20Web&firmware=web&appid=0&curday=&devicetoken=`. Success = `error:0` with `body` = BookingID. `error:100` means fully booked — report the queue option, never auto-join.
7. Cancel, only after user confirmation: the same call with `rebook=1&timeslot=` (empty) for that booking's laundryid and date. Success = `error:0`.
8. List current bookings: `method=getMyBooking&start=0&limit=50`.
9. After each booking or cancellation, report BookingID, room, date and slot to the user.

## Pitfalls

- The buildingid in login/room calls is the v1 id (from lookup `v1_building_id`), not the v2 search id; the v2 surface (`/api/v2/*`, `/auth/login`, `/auth/exchange`) does not work for v1-mode buildings.
- Slot ids are per room and date; multiple slots join with commas in `timeslot`.
- Redo login once if a call fails with an auth error; tokens are short-lived.
- URL-encode every param and keep `lang=1` on all calls.
- Booking3 and cancel are live-tested (2026-09-05: book → BookingID returned and slot showed as own → cancel → clean). On any error other than 0 (or 100=queue), stop and re-check the reference.
- Guest apartments, where a building has them, unlock with the same apartment PIN after booking.
- Respect building-specific booking rules from the user's memory when present.
