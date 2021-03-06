import factory
from app.models.access_code import db, AccessCode
from app.factories.ticket import TicketFactory
from app.factories.event import EventFactoryBasic
from app.factories.user import UserFactory
import app.factories.common as common


class AccessCodeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = AccessCode
        sqlalchemy_session = db.session

    tickets = factory.RelatedFactory(TicketFactory)
    event = factory.RelatedFactory(EventFactoryBasic)
    user = factory.RelatedFactory(UserFactory)
    code = common.string_
    access_url = common.url_
    is_active = True
    tickets_number = 10
    min_quantity = 10
    max_quantity = 100
    valid_from = common.date_
    valid_till = common.dateEnd_
    used_for = common.string_
    user_id = 2
