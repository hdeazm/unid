import web
import config
import json


class Api_productos:
    def get(self, id_producto):
        try:
            # http://0.0.0.0:8080/api_productos?user_hash=12345&action=get
            if id_producto is None:
                result = config.model.get_all_productos()
                productos_json = []
                for row in result:
                    tmp = dict(row)
                    productos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(productos_json)
            else:
                # http://0.0.0.0:8080/api_productos?user_hash=12345&action=get&id_producto=1
                result = config.model.get_productos(int(id_producto))
                productos_json = []
                productos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(productos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            productos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(productos_json)

# http://0.0.0.0:8080/api_productos?user_hash=12345&action=put&id_producto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, producto,existencias,precio):
        try:
            config.model.insert_productos(producto,existencias,precio)
            productos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(productos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_productos?user_hash=12345&action=delete&id_producto=1
    def delete(self, id_producto):
        try:
            config.model.delete_productos(id_producto)
            productos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(productos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_productos?user_hash=12345&action=update&id_producto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_producto, producto,existencias,precio):
        try:
            config.model.edit_productos(id_producto,producto,existencias,precio)
            productos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(productos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            productos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(productos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_producto=None,
            producto=None,
            existencias=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_producto=user_data.id_producto
            producto=user_data.producto
            existencias=user_data.existencias
            precio=user_data.precio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_producto)
                elif action == 'put':
                    return self.put(producto,existencias,precio)
                elif action == 'delete':
                    return self.delete(id_producto)
                elif action == 'update':
                    return self.update(id_producto, producto,existencias,precio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
