from .models import Company, MyUser
from rest_framework import serializers

class SingleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = ['password', 'is_admin','is_active','last_login']

    def to_representation(self, instance):
        ret =  super(SingleUserSerializer, self).to_representation(instance)
        comname = ret.pop('company')
        if comname is not None:
            com = Company.objects.get(pk=comname)
            userlinks = [
                ret.pop('linkedin'),
                ret.pop('github'),
                ret.pop('facebook'),
            ]
            ret['userlinks'] = userlinks
            ret['company'] = {
                "name":com.name,
                "summary":com.summary,
                "companylinks":[
                    com.linkedin, 
                    com.github,
                    com.facebook
                ]
            }
        else:
            ret['company'] = None
        return ret


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = ['password', 'is_admin','is_active','last_login']

    def to_representation(self, instance):
        ret =  super(UserSerialzer, self).to_representation(instance)
        com = ret.pop('company')
        if com is not None:
            ret['comapny'] = Company.objects.get(id=com).name
        else:
            ret['comapny'] = None
        links = [
            ret.pop("linkedin"),
            ret.pop("github"),
            ret.pop("facebook"),
        ]
        ret['links'] = links
        return ret



class SingleCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','summary','logo','linkedin','facebook','github']

    def to_representation(self, obj):
        ret = super(SingleCompanySerializer, self).to_representation(obj)
        company_id = ret.get("id")
        advocates = MyUser.objects.filter(company = company_id)
        linkedin = ret.pop('linkedin')
        github = ret.pop('github')
        facebook = ret.pop('facebook')
        ret['companylinks'] = {
            "linkedin": linkedin,
            "github": github,
            "facebook": facebook,
        }
        ret['advocates'] = []
        for adv in advocates:
            ret['advocates'].append(
                {"id":adv.id,
                "fname":adv.fname,
                "lname":adv.lname,
                "short_bio":adv.short_bio,
                "long_bio":adv.long_bio,
                "experience":adv.experience
                })
        return ret 

    

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id','name','summary','logo','linkedin','facebook','github']

    def to_representation(self, instance):
        ret =  super(CompanySerializer, self).to_representation(instance)
        links = [
            ret.pop("linkedin"),
            ret.pop("github"),
            ret.pop("facebook"),
        ]
        ret['links'] = links
        return ret