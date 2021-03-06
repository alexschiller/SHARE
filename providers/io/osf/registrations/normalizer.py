from share.normalize import ctx
from share.normalize.links import Delegate, Map, Maybe, Try, ParseDate

from providers.io.osf import normalizer as osf


class Registration(osf.Project):
    date_published = ParseDate(ctx.attributes.date_created)
    free_to_read_date = Try(ParseDate(ctx.attributes.embargo_end_date), exceptions=(ValueError, ))
    identifiers = Map(Delegate(osf.WorkIdentifier), ctx.links.html, ctx.links.self)

    class Extra:
        registration_schema = Maybe(ctx.relationships, 'registration_schema').links.related.href
        pending_registration_approval = Maybe(ctx.relationships, 'pending_registration_approval')
        registration_supplement = Maybe(ctx.attributes, 'registration_supplement')
        registered_meta_summary = Try(ctx.registered_meta.summary.value)
        withdrawn = Maybe(ctx.attributes, 'withdrawn')
        date_registered = Maybe(ctx.attributes, 'withdrawn')
        pending_embargo_approval = Maybe(ctx.attributes, 'pending_embargo_approval')
        withdrawal_justification = Maybe(ctx.attributes, 'withdrawal_justification')
        pending_withdrawal = Maybe(ctx.attributes, 'pending_withdrawal')
