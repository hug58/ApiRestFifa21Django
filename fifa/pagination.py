



from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


from rest_framework.exceptions import NotFound  
from rest_framework.exceptions import APIException




class NotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('bad_request.')
    default_code = 'bad_request'


class BasePagination(pagination.PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages


        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            # Here it is
            msg = {
                "code": 400, # you can remove this line as now the status code will be 400 by default as we have override it in `NotFound` class(see above)
                "error": "Page out of range"
            }
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)


    def get_paginated_response(self, data):
        return Response({
            #'links': {'next': self.get_next_link(),'previous': self.get_previous_link()},
            'totalItems': self.page.paginator.count,
            'Items': len(data),
            'totalPages': self.page.paginator.num_pages,
            'Page': self.page.number,   
            'results': data
        })


class TeamPagination(BasePagination):

    def get_page_number(self, request, paginator):
        page_number = request.query_params.get(self.page_query_param, 1)
        page_number = request.data.get('Page', page_number)

        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number
