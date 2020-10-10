# Generated by Django 3.1.2 on 2020-10-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnorms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boyd4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('low_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ovary_no', models.IntegerField(default=0)),
                ('ovary_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('f_tube_no', models.IntegerField(default=0)),
                ('f_tube_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uterus_no', models.IntegerField(default=0)),
                ('uterus_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Boyd56',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('low_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('adr_no', models.IntegerField(default=0)),
                ('adr_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hypo_no', models.IntegerField(default=0)),
                ('hypo_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('panc_no', models.IntegerField(default=0)),
                ('panc_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thyroid_no', models.IntegerField(default=0)),
                ('thyroid_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BoydIII',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('low_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_age', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brain_no', models.IntegerField(default=0)),
                ('brain_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lung_no', models.IntegerField(default=0)),
                ('lung_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('heart_no', models.IntegerField(default=0)),
                ('heart_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kidneys_no', models.IntegerField(default=0)),
                ('kidneys_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('liver_no', models.IntegerField(default=0)),
                ('liver_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spleen_no', models.IntegerField(default=0)),
                ('spleen_wgt', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('low_day', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='k_brain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='k_heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='l_kidney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='l_lung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='liver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='r_kidney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='r_lung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='scho_hrt_bh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgt_cm', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=20)),
                ('h_hgt', models.IntegerField(default=0)),
                ('hgt_in', models.IntegerField(default=0)),
                ('l95', models.IntegerField(default=0)),
                ('P', models.IntegerField(default=0)),
                ('u95', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='scho_hrt_bw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgt_cm', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=20)),
                ('h_hgt', models.IntegerField(default=0)),
                ('hgt_in', models.IntegerField(default=0)),
                ('l95', models.IntegerField(default=0)),
                ('P', models.IntegerField(default=0)),
                ('u95', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='scho_vent_val',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=20)),
                ('h_age', models.IntegerField(default=0)),
                ('rvl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rvp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rvu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lvl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lvp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lvu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sepl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sepp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sepu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avlp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avlu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mvl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mvp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mvu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pull95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pulp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pulu95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trl95', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tru95', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='schultz_heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_year', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('l_age', models.DecimalField(decimal_places=11, max_digits=13)),
                ('h_age', models.DecimalField(decimal_places=11, max_digits=13)),
                ('g_age', models.IntegerField()),
                ('b_wgt', models.IntegerField()),
                ('lgt', models.DecimalField(decimal_places=1, max_digits=7)),
                ('hrt_wgt', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lvt', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rvt', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tri', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pul', models.DecimalField(decimal_places=1, max_digits=7)),
                ('mit', models.DecimalField(decimal_places=1, max_digits=7)),
                ('aor', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='spleen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_days', models.DecimalField(decimal_places=11, max_digits=13)),
                ('sex', models.CharField(max_length=20)),
                ('n', models.IntegerField(default=0)),
                ('high_day', models.IntegerField(default=0)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mean_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ss_linbw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('l_weight', models.IntegerField()),
                ('h_weight', models.IntegerField()),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ss_linbwrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('l_weight', models.IntegerField()),
                ('h_weight', models.IntegerField()),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ss_linga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ss_lingarg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ss_sbga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='ss_sbgargs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='stinbw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('l_weight', models.IntegerField()),
                ('h_weight', models.IntegerField()),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='stinbwrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.CharField(max_length=20)),
                ('l_weight', models.IntegerField()),
                ('h_weight', models.IntegerField()),
                ('gestational_age', models.IntegerField()),
                ('crown_rump', models.DecimalField(decimal_places=1, max_digits=7)),
                ('crown_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('toe_heel', models.DecimalField(decimal_places=1, max_digits=7)),
                ('brain', models.DecimalField(decimal_places=1, max_digits=7)),
                ('thymus', models.DecimalField(decimal_places=1, max_digits=7)),
                ('heart', models.DecimalField(decimal_places=1, max_digits=7)),
                ('lungs_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('spleen', models.DecimalField(decimal_places=1, max_digits=7)),
                ('liver', models.DecimalField(decimal_places=1, max_digits=7)),
                ('kidneys_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('adrenals_combined', models.DecimalField(decimal_places=1, max_digits=7)),
                ('pancreas', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
    ]