<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Universal maps & navigation deep‑link reference** – a consolidated, source‑cited cheat‑sheet for the most common mapping apps.  

---

## 1. Feature inventory (what each app supports)

| App | Search | Directions / Navigation | Show location only | Travel‑mode values | Platform(s) | Fallback if app missing |
|---|---|---|---|---|---|---|
| **Google Maps** | ✅ `search` URL | ✅ `dir` URL | ✅ `@` map view | driving, walking, bicycling, transit ⚠️ CONFLICT (shard 2 also lists *two‑wheeler*) | Web, iOS, Android | Opens web map (browser) |
| **Apple Maps** | ✅ web & `maps://` | ✅ `daddr` / `/directions` | ✅ `ll` | driving, walking, transit, **bicycling** ⚠️ CONFLICT (shard 1 omits bicycling) | Web, iOS, macOS | Opens Apple Maps web UI |
| **Waze** | ✅ universal link | ✅ `navigate=yes` | ✅ `ll` | driving only (no mode param) | Web, iOS, Android | Web page with “Open in app” button |
| **Organic Maps** | ✅ short link & `om://` | – (no built‑in turn‑by‑turn) | ✅ both forms | – | iOS, Android, any browser (short link) | Short link redirects to app store if not installed |
| **CoMaps** | ✅ short link & `cm://` | – | ✅ both forms | – | iOS, Android, any browser (short link) | ⚠️ UNVERIFIED – no official docs |
| **HERE WeGo** | ✅ share link | ✅ `here-route://` (unverified) | ✅ `here-location://` (unverified) | car, pedestrian, bicycle, publicTransport | Web, iOS, Android | Share link opens web UI; scheme may fail silently |
| **Sygic** | – | ✅ `com.sygic.aura://coordinate|LON|LAT|TYPE` | ✅ both scheme & http fallback | drive, walk, bicycle, truck, motorcycle | iOS, Android | http fallback works on Android; otherwise nothing |
| **Android generic** | ✅ `geo:` | ✅ `google.navigation:` | ✅ `geo:` | driving, walking, bicycling, transit (via `mode` in navigation intent) | Android only | Chooser if no map app handles intent |
| **Windows Bing Maps** | – | ✅ `bingmaps:?cp=LAT~LON` (UWP) / web URL with `rtp` | ✅ `cp` | driving, transit, walking | Windows 10/11 (UWP) & any browser | Requires Bing Maps app or built‑in component |
| **OpenStreetMap** | – | ✅ web directions URL | ✅ web map view | driving (default) | Any browser | No native app deep‑link; only web UI |

---

## 2. Deep‑link templates (Action | Template | Parameters | Notes | Source)

### Google Maps
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Search / place | `https://www.google.com/maps/search/?api=1&query=QUERY` | `query` (required) – address, POI, or `lat,lng` | `api=1` mandatory; URL‑encode spaces/comma (`%2C`) | 【1】 |
| Directions (turn‑by‑turn) | `https://www.google.com/maps/dir/?api=1&origin=ORIGIN&destination=DEST&travelmode=MODE` | `origin` (optional `lat,lng`), `destination` (required `lat,lng`), `travelmode` (`driving` | `walking` | `bicycling` | `transit` | ⚠️ CONFLICT – shard 2 also lists `two-wheeler`) | Defaults to **driving** if omitted | 【1】 |
| Display map (center + zoom) | `https://www.google.com/maps/@?api=1&map_action=map&center=LAT,LNG&zoom=Z` | `center` (`lat,lng`), `zoom` (1‑21) | Shows map view only | 【1】 |
| iOS native scheme | `comgooglemaps://?daddr=LAT%2CLON&directionsmode=MODE` | `daddr` (`lat,lng`), `directionsmode` (`driving` | `walking` | `bicycling` | `transit`) | App must be installed; silent fail otherwise | 【2】 |
| Android intent – generic geo | `geo:LAT,LON?q=QUERY` | `q` (optional free‑text) | Opens chooser if no app handles intent | 【3】 |
| Android intent – navigation | `google.navigation:q=DEST_LAT,DEST_LON&mode=MODE` | `mode` (`d` driving | `w` walking | `b` bicycling | `t` transit) | Requires Google Maps app | 【3】 |

### Apple Maps
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Open location (web) | `https://maps.apple.com/?ll=LAT%2CLON` | `ll` (`lat,lng`) | Works on any platform; opens Apple Maps web UI | 【4】 |
| Open location (iOS scheme) | `maps://?ll=LAT%2CLON` | `ll` (`lat,lng`) | Requires app; silent fail otherwise | 【4】 |
| Directions (legacy) | `https://maps.apple.com/?daddr=DEST_LAT%2CDEST_LON&dirflg=MODE` | `daddr` (`lat,lng`), `dirflg` (`d` driving | `w` walking | `r` public‑transit | `t` taxi) | Single‑letter code; defaults to driving if missing/invalid | 【4】 |
| Directions (newer) | `https://maps.apple.com/directions?from=ORIGIN_LAT%2CORIGIN_LON&to=DEST_LAT%2CDEST_LON&travelmode=MODE` | `from`, `to`, `travelmode` (`driving` | `walking` | `transit` | `bicycling`) | Not all params documented for iOS 13+; test fallback | 【5】 |
| Search (web) | `https://maps.apple.com/?q=QUERY&ll=LAT,LNG&daddr=DEST&dirflg=MODE&t=MAPTYPE` | `q`, `ll`, `daddr`, `dirflg`, `t` (`m` standard | `k` satellite | `h` hybrid) | `daddr` required for directions; `ll` overrides address | 【4】 |
| iOS scheme (search) | `maps://?q=QUERY&ll=LAT,LNG&daddr=DEST&dirflg=MODE` | Same as web | Same notes | 【4】 |

### Waze
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Open location / start navigation (web) | `https://waze.com/ul?ll=LAT%2CLON&navigate=yes&zoom=Z` | `ll` (`lat,lng`), `navigate` (`yes` | `no`), `zoom` (1‑20) | If app installed, launches it; otherwise shows web page with “Open in app” | 【6】 |
| iOS / Android scheme | `waze://?ll=LAT%2CLON&navigate=yes` | Same as web | Silent fail if app missing | 【6】 |
| Optional search | `https://waze.com/ul?ll=LAT%2CLON&q=QUERY` | `q` (search term) | No travel‑mode param | 【6】 |

### Organic Maps
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Short‑link (browser) | `https://omaps.app/?ll=LAT%2CLON` | `ll` (`lat,lng`) | Redirects to app if installed; otherwise shows web page | 【7】 |
| Deep‑link (in‑app) | `om://?ll=LAT%2CLON` | `ll` (`lat,lng`) | Requires app; otherwise ignored | 【7】 |
| Alternative short‑link format | `https://omaps.app/LAT,LNG/NAME` | `NAME` (optional label) | Human‑readable URL | 【7】 |
| Geo URI (fallback) | `geo:LAT,LNG` or `geo:0,0?q=LAT,LNG(LABEL)` | Standard `geo:` format | Works with many map apps | 【7】 |

### CoMaps (fork of Organic Maps)
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Short‑link (browser) | `https://comaps.at/?lat=LAT&lon=LON` | `lat`, `lon` | Works cross‑platform | ⚠️ UNVERIFIED – no official docs found |
| Deep‑link (in‑app) | `cm://map?v=1&ll=LAT%2CLON&n=NAME` | `ll`, `n`, `v` | Same scheme as Organic Maps | ⚠️ UNVERIFIED |
| Geo URI | `geo:LAT,LON` | – | Standard fallback | ⚠️ UNVERIFIED |

### HERE WeGo
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Share map view (web) | `https://share.here.com/?mapview=LAT%2CLON` | `mapview` (`lat,lng`) | Opens HERE WeGo web UI; may prompt to open app | 【8】 |
| Turn‑by‑turn (scheme) | `here-route://?from=ORIGIN_LAT%2CORIGIN_LON&to=DEST_LAT%2CDEST_LON&mode=MODE` | `from`, `to`, `mode` (`car` | `pedestrian` | `bicycle` | `publicTransport`) | **UNVERIFIED** – mentioned in forums, not in public docs | ⚠️ CONFLICT (shard 1 UNVERIFIED, shard 2 provides StackOverflow example) |
| Location scheme | `here-location://?lat=LAT&lng=LON` | `lat`, `lng` | Same as above | ⚠️ UNVERIFIED |

### Sygic
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| In‑app scheme (iOS/Android) | `com.sygic.aura://coordinate|LON|LAT|TYPE` | Pipe‑separated: `LON|LAT|drive|walk|bicycle|truck|motorcycle` | **Order is longitude first**; silent fail if app missing | 【9】 |
| HTTP fallback | `http://com.sygic.aura/?coordinate=LON%2CLAT&mode=MODE` | `coordinate` (`lon,lat`), `mode` (`drive` | `walk` | …) | Works on Android when scheme blocked | 【9】 |
| Web navigation (fallback) | `https://go.sygic.com/directions?to=LAT,LNG` | `to` (`lat,lng`) | Opens web page; can redirect to app store | ⚠️ UNVERIFIED (source is StackOverflow) |

### Android generic geo intent
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Show location / search | `geo:LAT,LONG?q=QUERY` | `q` (optional free‑text) | Opens chooser if no app handles intent | 【3】 |
| Start navigation | `google.navigation:q=DEST_LAT,DEST_LON&mode=MODE` | `mode` (`d` driving | `w` walking | `b` bicycling | `t` transit) | Requires Google Maps app | 【3】 |

### Windows Bing Maps
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Open location (UWP) | `bingmaps:?cp=LAT~LON` | `cp` (`lat~lon`) | Requires Bing Maps app or built‑in component | 【10】 |
| Web route URL | `https://bing.com/maps/default.aspx?rtp=adr.ADDRESS1~adr.ADDRESS2&rtop=0~1~0&mode=D` | `rtp` (route points), `mode` (`D` driving | `T` transit | `W` walking) | Works in any browser | 【10】 |

### OpenStreetMap
| Action | Template | Parameters | Notes | Source |
|---|---|---|---|---|
| Directions (web) | `https://www.openstreetmap.org/directions?route=ORIGIN_LAT%2CORIGIN_LON%3BDEST_LAT%2CDEST_LON` | `route` (`lat,lon;lat,lon`) – semicolon separates way‑points | Driving by default; URL‑encode `;` as `%3B` | 【11】 |
| Map view (web) | `https://www.openstreetmap.org/#map=ZOOM/LAT/LON` | `map=ZOOM/LAT/LON` | Standard OSM map view | 【11】 |

---

## 3. How to choose & use

1. **Detect platform / installed app** – e.g., `canOpenURL` on iOS, `PackageManager.resolveActivity` on Android.  
2. **Pick the appropriate template** from the table above for the desired action (search, show location, navigation).  
3. **Insert real values** (lat, lon, query, etc.) into the placeholders (uppercase in the tables).  
4. **URL‑encode** special characters (`%2C` for commas, `%20` for spaces, `%3B` for semicolons).  
5. **Send the final URL** to the client. If the native scheme fails, fall back to the web version (most tables list a web fallback).  

---

## Sources

1. Google Maps URLs – Get Started: <https://developers.google.com/maps/documentation/urls/get-started>  
2. Google Maps iOS URL Scheme: <https://developers.google.com/maps/documentation/urls/ios>  
3. Android Intents – Common: <https://developer.android.com/guide/components/intents-common#geo>  
4. Apple Maps URL Scheme (legacy): <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/Maps/URL%20Schemes/URLSchemes.html>  
5. Apple Maps URL Scheme – Updated (2022): <https://developer.apple.com/documentation/mapsurl>  
6. Waze URL Scheme (official wiki): <https://waze.com/wiki/URL_scheme>  
7. Organic Maps – README (deep‑link info): <https://github.com/organicmaps/organicmaps/blob/master/README.md>  
8. HERE WeGo – Share Links: <https://developer.here.com/documentation/links/overview.html>  
9. Sygic – URL Scheme Documentation: <https://www.sygic.com/en/docs/developers/url-scheme>  
10. Bing Maps URI Scheme (UWP): <https://learn.microsoft.com/en-us/windows/uwp/maps-and-location/bing-maps-uri-scheme>  
11. OpenStreetMap – Directions URL: <https://wiki.openstreetmap.org/wiki/OSM_URL_Schemes#Directions>  

*Additional secondary references used in the second shard (e.g., StackOverflow, developer.here.com, etc.) are omitted here because official docs were preferred where available.*
