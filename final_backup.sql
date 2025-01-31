PGDMP  $    3                 |         
   art school    16.2    16.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16394 
   art school    DATABASE     �   CREATE DATABASE "art school" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "art school";
                postgres    false            �            1259    16395    classes    TABLE       CREATE TABLE public.classes (
    class_id integer NOT NULL,
    date date NOT NULL,
    "time" time without time zone NOT NULL,
    classroom_no integer NOT NULL,
    group_no integer NOT NULL,
    empl_contract_no integer NOT NULL,
    subject_id integer NOT NULL
);
    DROP TABLE public.classes;
       public         heap    postgres    false            �            1259    16400    groups    TABLE     �   CREATE TABLE public.groups (
    group_no integer NOT NULL,
    field_of_study character varying NOT NULL,
    year_of_study integer NOT NULL
);
    DROP TABLE public.groups;
       public         heap    postgres    false            �            1259    16405    students    TABLE       CREATE TABLE public.students (
    enrollment_order_no integer NOT NULL,
    full_name character varying NOT NULL,
    date_of_birth date NOT NULL,
    parents_contact_info_1 character varying NOT NULL,
    parents_contact_info_2 character varying,
    group_no integer NOT NULL
);
    DROP TABLE public.students;
       public         heap    postgres    false            �            1259    16643    subjects    TABLE     �   CREATE TABLE public.subjects (
    uid integer NOT NULL,
    name character varying NOT NULL,
    hours_of_study integer NOT NULL
);
    DROP TABLE public.subjects;
       public         heap    postgres    false            �            1259    16415    teachers    TABLE     �   CREATE TABLE public.teachers (
    empl_contract_no integer NOT NULL,
    full_name character varying NOT NULL,
    passport_serial integer NOT NULL,
    passport_number integer NOT NULL,
    subject character varying NOT NULL
);
    DROP TABLE public.teachers;
       public         heap    postgres    false            �          0    16395    classes 
   TABLE DATA           o   COPY public.classes (class_id, date, "time", classroom_no, group_no, empl_contract_no, subject_id) FROM stdin;
    public          postgres    false    215   �       �          0    16400    groups 
   TABLE DATA           I   COPY public.groups (group_no, field_of_study, year_of_study) FROM stdin;
    public          postgres    false    216   "       �          0    16405    students 
   TABLE DATA           �   COPY public.students (enrollment_order_no, full_name, date_of_birth, parents_contact_info_1, parents_contact_info_2, group_no) FROM stdin;
    public          postgres    false    217   �                  0    16643    subjects 
   TABLE DATA           =   COPY public.subjects (uid, name, hours_of_study) FROM stdin;
    public          postgres    false    219   `       �          0    16415    teachers 
   TABLE DATA           j   COPY public.teachers (empl_contract_no, full_name, passport_serial, passport_number, subject) FROM stdin;
    public          postgres    false    218   �       `           2606    16605    classes classes_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_pkey PRIMARY KEY (class_id);
 >   ALTER TABLE ONLY public.classes DROP CONSTRAINT classes_pkey;
       public            postgres    false    215            b           2606    16423    groups groups_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (group_no);
 <   ALTER TABLE ONLY public.groups DROP CONSTRAINT groups_pkey;
       public            postgres    false    216            d           2606    16626    students students_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (enrollment_order_no);
 @   ALTER TABLE ONLY public.students DROP CONSTRAINT students_pkey;
       public            postgres    false    217            h           2606    16649    subjects subjects_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (uid);
 @   ALTER TABLE ONLY public.subjects DROP CONSTRAINT subjects_pkey;
       public            postgres    false    219            f           2606    16429    teachers teachers_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (empl_contract_no);
 @   ALTER TABLE ONLY public.teachers DROP CONSTRAINT teachers_pkey;
       public            postgres    false    218            i           2606    16610    classes from group    FK CONSTRAINT     �   ALTER TABLE ONLY public.classes
    ADD CONSTRAINT "from group" FOREIGN KEY (group_no) REFERENCES public.groups(group_no) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 >   ALTER TABLE ONLY public.classes DROP CONSTRAINT "from group";
       public          postgres    false    216    215    4706            j           2606    16650    classes from subject    FK CONSTRAINT     �   ALTER TABLE ONLY public.classes
    ADD CONSTRAINT "from subject" FOREIGN KEY (subject_id) REFERENCES public.subjects(uid) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 @   ALTER TABLE ONLY public.classes DROP CONSTRAINT "from subject";
       public          postgres    false    215    4712    219            k           2606    16620    classes from teacher    FK CONSTRAINT     �   ALTER TABLE ONLY public.classes
    ADD CONSTRAINT "from teacher" FOREIGN KEY (empl_contract_no) REFERENCES public.teachers(empl_contract_no) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 @   ALTER TABLE ONLY public.classes DROP CONSTRAINT "from teacher";
       public          postgres    false    218    4710    215            l           2606    16627    students students_group_no_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_group_no_fkey FOREIGN KEY (group_no) REFERENCES public.groups(group_no) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 I   ALTER TABLE ONLY public.students DROP CONSTRAINT students_group_no_fkey;
       public          postgres    false    217    216    4706            �   A   x�%�� !�7䢵쁢���e�<�BЛ��ja53��bj!�����b�L�POW�&-G      �   ]   x���� E��LV`�X�KЀ�R�A�WÛ�����	Y����(�eǫZ:��K�Dmŉ�F�$T�p!�aC�Yo��4��3��1~      �   �   x�U�KnB1E��*�����9{�b
BbʠC$P7P����
��fG8&�Ɩ����D���f<p���8p��טps�}�=�b�;�!4O�S4�1�RSZ��ҘYi52I68��7�s�p�Rڴ|'�:��z�}�E���Ti%/���M��"�{���8a��d���'VAQ�Ē��9��,Ie?V��'�z�          <   x�3估��.컰���{8��,��8/6�v_��ra�-@E�8���b���� gc      �   �   x�-NK�0\���(-��xE.\��@�(�+̻�S�o�:�7S_T�
���0a��G~<u�3n�Ip��@��������$/\*�r��������>R�Nx�P�:���ŀ�����ģ��IfC�:њ�p��%T�`4,�ˬ����;)�����䛱[m�ze�� w�8     