from share.normalize import *
from share.normalize import links


class Organization(Parser):
    name = OneOf(Try(ctx.name), ctx)

    # class Extra:
    #     doi = Maybe(ctx, 'DOI')
    #     award = Maybe(ctx, 'award')
    #     doi_asserted_by = Maybe(ctx, 'doi-asserted-by')


class FundingContribution(Parser):
    entity = Delegate(Organization, ctx)


class PublishingContribution(Parser):
    entity = Delegate(Organization, ctx)


class PersonIdentifier(Parser):
    uri = Orcid(ctx)


class WorkIdentifier(Parser):
    uri = DOI(ctx)


class Person(Parser):
    given_name = Maybe(ctx, 'given')
    family_name = Maybe(ctx, 'family')
    # affiliations = Map(Delegate(Affiliation.using(entity=Delegate(Organization))), Maybe(ctx, 'affiliation'))
    identifiers = Map(Delegate(PersonIdentifier), Maybe(ctx, 'ORCID'))


class Contribution(Parser):
    entity = Delegate(Person, ctx)
    order_cited = ctx('index')

    cited_as = links.Join(
        Concat(
            Maybe(ctx, 'given'),
            Maybe(ctx, 'family')
        ),
        joiner=' '
    )


class Tag(Parser):
    name = ctx


class ThroughTags(Parser):
    tag = Delegate(Tag, ctx)


class CreativeWork(Parser):
    """
    Documentation for CrossRef's metadata can be found here:
    https://github.com/CrossRef/rest-api-doc/blob/master/api_format.md
    """

    def get_schema(self, type):
        return {
            'journal-article': 'Article',
            'book': 'Book',
            'proceedings-article': 'ConferencePaper',
            'dataset': 'Dataset',
            'dissertation': 'Dissertation',
            'preprint': 'Preprint',
            'report': 'Report',
            'book-section': 'Section',
        }.get(type) or 'CreativeWork'

    schema = RunPython('get_schema', ctx.type)

    title = Maybe(ctx, 'title')[0]
    description = Maybe(ctx, 'subtitle')[0]
    date_updated = ParseDate(Try(ctx.deposited['date-time']))

    # contributors = Map(
    #     Delegate(Contributor),
    #     Maybe(ctx, 'author')
    # )

    identifiers = Map(Delegate(WorkIdentifier), ctx.DOI)

    related_entities = Concat(
        Map(Delegate(Contribution), Try(ctx.author)),
        Map(Delegate(PublishingContribution), ctx.publisher),
        Map(Delegate(FundingContribution), Try(ctx.funder)),
    )
    # publishers = Map(
    #     Delegate(Association.using(entity=Delegate(Publisher))),
    #     ctx.publisher
    # )
    # funders = Map(
    #     Delegate(Association.using(entity=Delegate(Funder))),
    #     Maybe(ctx, 'funder')
    # )
    # TODO These are "a controlled vocabulary from Sci-Val", map to Subjects!
    tags = Map(
        Delegate(ThroughTags),
        Maybe(ctx, 'subject')
    )

    class Extra:
        alternative_id = Maybe(ctx, 'alternative-id')
        archive = Maybe(ctx, 'archive')
        article_number = Maybe(ctx, 'article-number')
        chair = Maybe(ctx, 'chair')
        container_title = Maybe(ctx, 'container-title')
        date_created = ParseDate(Try(ctx.created['date-time']))
        date_published = Maybe(ctx, 'issued')
        editor = Maybe(ctx, 'editor')
        licenses = Maybe(ctx, 'license')
        isbn = Maybe(ctx, 'isbn')
        issn = Maybe(ctx, 'issn')
        issue = Maybe(ctx, 'issue')
        member = Maybe(ctx, 'member')
        page = Maybe(ctx, 'page')
        published_online = Maybe(ctx, 'published-online')
        published_print = Maybe(ctx, 'published-print')
        reference_count = ctx['reference-count']
        subjects = Maybe(ctx, 'subject')
        subtitles = Maybe(ctx, 'subtitle')
        titles = ctx.title
        translator = Maybe(ctx, 'translator')
        type = ctx.type
        volume = Maybe(ctx, 'volume')
