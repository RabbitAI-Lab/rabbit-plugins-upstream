# Deep links — verified templates for all 7 apps (+ open fallbacks)

Every template here was checked against the vendor's own documentation (source column) and is
what `scripts/deeplinks.py` generates. Coordinates are `LAT,LON` everywhere **except Sygic (LON before LAT)**.
Encode `|` as `%7C` and `,` as `%2C` in query values where the vendor says so (Google, Sygic-iOS).

## Start navigation to a point

| App | Template | Modes | Origin / waypoints | Source |
|---|---|---|---|---|
| Google Maps | `https://www.google.com/maps/dir/?api=1&destination=LAT,LON&travelmode=driving&dir_action=navigate[&origin=…][&waypoints=a%7Cb][&avoid=tolls,highways,ferries]` | `driving walking bicycling two-wheeler transit` | origin optional (= current), ≤9 waypoints (3 on mobile web), 2048-char limit | developers.google.com/maps/documentation/urls/get-started |
| Google Maps (iOS scheme) | `comgooglemaps://?daddr=LAT,LON[&saddr=…]&directionsmode=driving\|walking\|bicycling\|transit` | 4 | — | developers.google.com/maps/documentation/urls/ios-urlscheme |
| Google Maps (Android intent) | `google.navigation:q=LAT,LON&mode=d\|w\|b\|l` | d=drive w=walk b=bike l=two-wheeler | starts guidance immediately | developer.android.com/guide/components/google-maps-intents |
| Apple Maps | `https://maps.apple.com/?daddr=LAT,LON&dirflg=d\|w\|r[&saddr=…][&t=m\|k\|h\|r]` (same params on `maps://`) | d=drive w=walk r=transit (c=cycling: third-party documented) | origin optional, no waypoints | developer.apple.com/library/archive/…/MapLinks |
| Waze | `https://waze.com/ul?ll=LAT,LON&navigate=yes&zoom=17[&utm_source=…]` · `?q=<text>&navigate=yes` · `?favorite=home\|work&navigate=yes` | driving only | always from current position, no waypoints; `waze://` only if app guaranteed | developers.google.com/waze/deeplinks |
| Organic Maps | `om://route?sll=LAT,LON&saddr=Name&dll=LAT,LON&daddr=Name&type=vehicle\|pedestrian\|bicycle\|transit` · `https://omaps.app/route?…` | 4 | start required in `route`; `om://v2/nav?origin=currentLocation&destination=LAT,LON&mode=drive\|walk\|bike\|transit[&waypoints=a\|b&waypoint_names=…]` adds waypoints + auto-start | omaps.app/api |
| CoMaps | identical to Organic Maps with `cm://` (or `comaps://`) and `https://comaps.at/route?…` | 4 | as above | comaps.at/api |
| HERE WeGo | `https://share.here.com/r/{ORIGIN}/{VIA…}/{DEST}?m=d\|w\|pt\|b\|cs\|t\|tr[&a=tollroad,motorway,boatFerry…][&z=][&ref=]` — each point `LAT,LON[,TITLE[,p]]`, origin may be `mylocation` | d car · w walk · pt transit · b bike · cs car-share · t taxi · tr truck (WeGo Pro) | 2–100 points (soft 50), `,p` = pass-through; Pro truck params `vdh vdl vdw vw`(cm/kg) `hmr=explosive,gas,flammable,organic,corrosive` `tcr=b` `trt=tractor\|straight` `trlc axc wpax` | docs.here.com/wego-pro/docs/share-route-dl |
| Sygic | `com.sygic.aura://coordinate\|LON\|LAT\|drive\|walk\|show` — via points: `coordinate\|viaLon\|viaLat\|…\|LON\|LAT\|drive`; address: `com.sygic.aura://address\|Country\|City\|Postal\|Street\|No\|drive` | drive walk show | unlimited via points; iOS: `%7C` for pipes; obsolete `http://com.sygic.aura/…` form still parsed | dev.sygic.com custom-url-schema (archived), SO 20784681 |
| OpenStreetMap web | `https://www.openstreetmap.org/directions?engine=fossgis_osrm_car\|bike\|foot&route=LAT,LON;LAT,LON` | 3 (+valhalla engines) | origin required | openstreetmap.org |
| Any app (RFC 5870) | `geo:LAT,LON?q=LAT,LON(Label)` · `geo:0,0?q=<search>` | — | Android/Linux default map app | RFC 5870 |

## Show / share a place

| App | Template | Source |
|---|---|---|
| Google | `https://www.google.com/maps/search/?api=1&query=LAT,LON[&query_place_id=]` · map view `…/maps/@?api=1&map_action=map&center=LAT,LON&zoom=Z&basemap=roadmap\|satellite\|terrain&layer=none\|transit\|traffic\|bicycling` · Street View `map_action=pano&viewpoint=LAT,LON[&heading&pitch&fov]` | Maps URLs |
| Apple | `https://maps.apple.com/?ll=LAT,LON&z=2-21[&q=Label][&t=m\|k\|h]` · search `?q=…&sll=LAT,LON` | MapLinks |
| Waze | `https://waze.com/ul?ll=LAT,LON&zoom=17` · web `https://www.waze.com/live-map/directions?to=ll.LAT%2CLON` | Waze deeplinks |
| Organic Maps | `om://map?v=1&ll=LAT,LON&n=Name` (repeat `ll&n` for several pins) · `https://omaps.app/map?…` · short links `https://omaps.app/<code>/<Name>` · `om://search?cll=LAT,LON&query=…` · `om://crosshair?cll=` | omaps.app/api |
| CoMaps | `cm://map?v=1&ll=…` · `https://comaps.at/map?…` · `https://comaps.at/<code>` | comaps.at/api |
| HERE WeGo | `https://share.here.com/l/LAT,LON[,Title]?z=16&t=normal\|satellite\|terrain\|traffic` · place `…/p/<placeId>` · search `…/s/<query>` | docs.here.com |
| Sygic | `com.sygic.aura://coordinate\|LON\|LAT\|show` | Sygic |
| OSM | `https://www.openstreetmap.org/?mlat=LAT&mlon=LON#map=16/LAT/LON` (`&layers=N` = notes) | OSM |

## Rejected (hallucinated by one research shard, absent from official docs)
`om://?ll=` · CoMaps `?lat=&lon=` · `here-route://` / `here-location://` (obsolete since WeGo 4) · Sygic `http://` form as primary.
