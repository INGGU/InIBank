# Generated by Django 4.2.7 on 2023-11-15 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MortgageLoansProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('loan_inci_expn', models.TextField()),
                ('erly_rpay_fee', models.TextField()),
                ('dly_rate', models.TextField()),
                ('loan_lmt', models.TextField()),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeDepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeDepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.timedepositproduct')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('rsrv_type', models.TextField()),
                ('rsrv_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.savingsproduct')),
            ],
        ),
        migrations.CreateModel(
            name='MortgageLoansOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('mrtg_type', models.TextField()),
                ('mrtg_type_nm', models.TextField()),
                ('rpay_type', models.TextField(null=True)),
                ('rpay_type_nm', models.TextField(null=True)),
                ('lend_rate_type', models.TextField()),
                ('lend_rate_type_nm', models.TextField()),
                ('lend_rate_min', models.FloatField()),
                ('lend_rate_max', models.FloatField()),
                ('lend_rate_avg', models.FloatField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.mortgageloansproduct')),
            ],
        ),
    ]
