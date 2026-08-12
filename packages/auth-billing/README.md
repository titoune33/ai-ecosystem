# auth-billing — Spec

Auth + paiement partagés. Déjà éprouvés dans Libera RH (auth par cookie,
Stripe) et saaskit (NextAuth + Stripe).

## Périmètre

- **Auth** : session cookie (httpOnly), login email+mot de passe, magic link optionnel.
- **Billing** : abonnements Stripe (Checkout, webhooks, portail client), plans
  mensuel/annuel, annulation 1 clic, CGV alignées.
- **Multi-tenant** : un client = un espace cloisonné (exigence métier RH : pas de
  contamination de contexte entre clients — cf. guide DRH).

## API cible

```ts
import { auth, billing } from "@titouane33/auth-billing";

const session = await auth.require(req);          // 401 sinon
const plan = await billing.getPlan(session.userId);
await billing.createCheckout({ userId, plan: "pro", interval: "month" });
```

## Exigences

- Webhooks Stripe idempotents, vérification de signature.
- Seuls les admins (rôle) voient les données multi-clients.
- Migration depuis les implémentations existantes (Libera RH, saaskit) sans
  casser les abonnés actuels.
