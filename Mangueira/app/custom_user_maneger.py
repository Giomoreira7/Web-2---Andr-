from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, password, cpf, rg,
                    address_street, address_district, address_number,
                    address_zip_code, address_city, address_state, 
                    address_country, **extra_fields):

        # Validate required fields
        if None in (name, email, password, cpf, rg,
                    address_street, address_district, address_number,
                    address_zip_code, address_city, address_state, 
                    address_country):
            raise ValueError('Missing required fields!')

    

    def create_superuser(self, name, email, password, cpf, rg,
                         address_street, address_district, address_number,
                         address_zip_code, address_city, address_state, 
                         address_country, **extra_fields):

        
    
        return self.create_user(
            name, email, password, cpf, rg,
            address_street, address_district, address_number,
            address_zip_code, address_city, address_state, 
            address_country, **extra_fields
        )