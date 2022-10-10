# pythonAutomation
MÜZİK KURSU-KURSİYER KAYIT OTOMASYONU
Bugün yeni bir iş aldım ve hemen bir program hazırlamaya çalıştım. Müşterimin benden talebi şuydu;
TALEP: Bir müzik kursu açacağım. Bu sebeple öğrencilerimin bilgilerinin kaydedildiği bir programa ihtiyacım var. Kaydedilecek bilgiler öğrenci adı soy adı ve yaşı olacak. Ayrıca bu programda kurs adları listelenmeli. Fiyatlandırma da seçtiğim kursa göre hesaplanmalı. Son olarak fiyatlandırmada 20 yaş altına 50 TL indirim yapılmalı.
Ben de projemin özelliklerini ve sınırlarını belirledim. Bana taslak olan bu özellikler doğrultusunda program hazırlamaya başladım.
ÖZELLİKLER
▪ Menüde while döngüsü olacak (kişi çıkmak istemediği sürece programdan çıkamayacak).
Ekleme Fonksiyonu Özellikleri
• Kaydedilmek istenilen öğrencinin bilgileri alınır. (adı_soyadı, yaşı, id)
• Burada her kaydedilen öğrenci için id numarası farklı girilmek zorundadır.
• Alınan bilgiler (main fonksiyonunda tanımlanmış pointer ile) bellekte ayrılan boş alana
atanır. Böylece kullanıcıdan alınan bilgiler hafızada tutulmuş olur.
Listeleme Fonksiyonu Özelikleri
• Ekle fonksiyonuyla alınan ve bellekte tutulan bilgilerin tamamı listelenir.
• Sil fonksiyonunda seçilen öğrenciler listelenmez.
Günceleme Fonksiyonu Özellikleri
• Güncellenmek istenen öğrencinin id numarası alınır.
• Güncellenmek istenen kişinin bilgileri yeniden girilir. (adı - soyadı, yaş)
Silme Fonksiyonu Özellikleri
• Kayıt silme için silinmek istenen kişinin id numarası alınır.
• Eğer kullanıcının girdiği id listede kayıtlı bir id ise girilen id 0 a eşitlenir.
Kurs Görme Fonksiyonu Özellikleri
• Struct ile tutulan kurs isimleri seviyesiyle beraber sırayla listelenir.
Kurs Fiyat Fonksiyonu Özellikleri
• Seçilen bu fonksiyonda kurs gör fonksiyonundaki listelenmiş olan fonksiyonlar ekranda yazdırılmıştır. Bu yazdırılan fonksiyonlardan istenen fonksiyon seçilir.
• Fiyatlandırma için yaş bilgisinin girilmesi gerekir. Fiyatlandırmada 20 yaş altına indirimli yapılmaktadır. 
