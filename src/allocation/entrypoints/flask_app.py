from src.allocation.adapters.repository import SqlAlchemyRepository
import flask


# @flask.route.gubbins
# def allocate_endpoint():
#     batches = SqlAlchemyRepository.list()
#     lines = [
#         OrderLine(l['orderid'], l['sku'], l['qty'])
#          for l in request.params...
#     ]
#     allocate(lines, batches)
#     session.commit()
#     return 201