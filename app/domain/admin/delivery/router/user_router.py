from app.domain.admin.delivery.impl.user_delivery_impl import UserDeliveryImplementation

delivery = UserDeliveryImplementation()
router = delivery.get_router()
