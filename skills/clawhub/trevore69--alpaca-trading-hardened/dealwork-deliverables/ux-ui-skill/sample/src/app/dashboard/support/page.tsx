import { CONFIG } from 'src/config-global';

import { SupportListView } from 'src/sections/support/view';

// ----------------------------------------------------------------------

export const metadata = { title: `Support tickets - ${CONFIG.appName}` };

export default function Page() {
  return <SupportListView />;
}
