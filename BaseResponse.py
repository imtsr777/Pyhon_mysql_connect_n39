
class BaseResponse:

    data = None

    error = None

    



select * from students where 
                                case when length('co')>0 
                                then firstName like '%co%'
                                else true end order by date desc 
                                offset $2 limit $3`,id,((page - 1) * limit), limit)